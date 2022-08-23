import inspect
from bottle import request, response, load, PluginError
from extra import FilesystemSessionStore

def _calls_update(name):
	def oncall(self, *args, **kw):
		rv = getattr(super(ModificationTrackingDict, self), name)(*args, **kw)

		if self.on_update is not None:
			self.on_update()

		return rv

	oncall.__name__ = name
	return oncall


class ModificationTrackingDict(dict):
	__slots__ = ("modified",)

	def __init__(self, *args, **kwargs):
		self.modified = False
		dict.update(self, *args, **kwargs)

	def on_update(self):
		self.modified = True

	def copy(self):
		"""Create a flat copy of the dict."""
		missing = object()
		result = self.__class__.__new__(self)
		for name in self.__slots__:
			val = getattr(self, name, missing)
			if val is not missing:
				setattr(result, name, val)
		return result

	def setdefault(self, key, default=None):
		modified = key not in self
		rv = super().setdefault(key, default)
		if modified and self.on_update is not None:
			self.on_update(self)
		return rv

	def pop(self, key, default=None):
		modified = key in self
		if default is None:
			rv = super().pop(key)
		else:
			rv = super().pop(key, default)
		if modified and self.on_update is not None:
			self.on_update()
		return rv

	__setitem__ = _calls_update("__setitem__")
	__delitem__ = _calls_update("__delitem__")
	clear = _calls_update("clear")
	popitem = _calls_update("popitem")
	update = _calls_update("update")

	def __copy__(self):
		return self.copy()

	def __repr__(self):
		return f"<{type(self).__name__} {dict.__repr__(self)}>"


class Session(ModificationTrackingDict):
	"""Subclass of a dict that keeps track of direct object changes.
	Changes in mutable structures are not tracked, for those you have to
	set ``modified`` to ``True`` by hand.
	"""

	__slots__ = ModificationTrackingDict.__slots__ + ("sid", "new", "_deleted")

	def __init__(self, data, sid, new=False):
		super(Session, self).__init__(data)
		self.sid = sid
		self.new = new
		self._deleted = False

	def __repr__(self):
		return "{}({}{})".format(
			self.__class__.__name__,
			dict.__repr__(self),
			"*" if self.should_save else "",
		)
	
	def __getitem__(self, item):
		if type(item) is tuple and len(item) > 1:
			try:
				key = item[0]
				data = super().__getitem__(item[0])
			except:
				return item[1]
		else:
			key = item
			data = super().__getitem__(item)
			if type(data) is dict and "_" in data and "__" in data:
				data["___"] = int(data["___"]) + 1
				if data["__"] == data["___"]:
					data = self.pop(key)
			return data
	
	def limit(self, name, lim):
		if name in self:
			self[name] = {"_": self[name], "__": lim, "___": 0}

	@property
	def should_save(self):
		"""True if the session should be saved."""
		return self.modified
	
	def delete(self):
		copy = [x for x in self]
		for x in copy:
			self.pop(x)
		self._deleted = True
	
	def __del__(self):
		self.delete()

class SessionPlugin:
	name = "session"
	api = 2

	def __init__(self, keyword="session", **kw):
		self.keyword = keyword
		self.session = None
		self.store = None
		self.kw = kw

	def get(self):
		sid = request.get_cookie(self.config.get('session.name', '_session_id'), secret=self.config.get('session.secret', 'wsgic_default_secret_key-jufjjgvssbionit4e4we6jbd4ri9k8'))

		if sid:
			self.session = self.store.get(sid)
		else:
			self.session = self.store.new()
		request.__dict__['session'] = self.session

	def save(self):
		if self.session.should_save:
			self.store.save(self.session)
			response.set_cookie(self.config.get('session.name', '_session_id'), self.session.sid, secret=self.config.get('session.secret', 'wsgic_default_secret_key-jufjjgvssbionit4e4we6jbd4ri9k8'))
		if self.session._deleted is True:
			self.store.delete(self.session)
			response.delete_cookie(self.config.get('session.name', '_session_id'))
			return

	def setup(self, app):
		for other in app.plugins:
			if not isinstance(other, SessionPlugin):
				continue
			if other.keyword == self.keyword:
				raise PluginError("Found another session plugin with  similiar keyword. You probably installed the plugin twice.")
		self.config = app.config
		sclass = app.config.get('session.class', Session)
		if type(sclass) is str:
			sclass = load(sclass)

		self.store = app.config.get('session.store', FilesystemSessionStore)
		if type(self.store) is str:
			self.store = load(self.store)
		self.store = self.store(session_class=sclass, **self.kw)
		app.hook('before_request')(self.get)
		app.hook('after_request')(self.save)

	def apply(self, callback, route):
		if self.keyword not in inspect.getargspec(route.callback)[0]:
			return callback

		def wrapper(*args, **kwargs):
			kwargs[self.keyword] = self.session
			return callback(*args, **kwargs)

		return wrapper

