__all__ = ["_get", "Router", "SqlalchemyDatabase"]

import sys
from threading import Thread

def load_module(target, **namespace):
	module, target = target.split(":", 1) if ':' in target else (target, None)
	if module not in sys.modules: __import__(module)
	if not target: return sys.modules[module]
	if target.isalnum(): return getattr(sys.modules[module], target)
	package_name = module.split('.')[0]
	namespace[package_name] = sys.modules[package_name]
	return eval('%s.%s' % (module, target), namespace)


def _get(data, index=0, e=None):
	try:return data[index] if type(data) in (list, dict, set, tuple) else data
	except:return e

class Router:
	'''
Router to handle routes
Adds the set namespace to all route set by the class instance

Parameters:
  During Creation:
	base url: '/auth'
	base route: usually Bottle.route or route or <Your Bottle instance>.route
	routes (optional): a list of your app routes
	
  Calling route and new method:
	the default routes arguments i.e path, method, name, function, skip etc

Usage:
	Router.route:
		auth = Router('/auth', route)
		@auth.route(url='/login', method="GET")
		def login():
			...
	
		produces:
			route('/auth/login', method="GET")
			
	
	Router.new and Router.router:
		auth = Router('/auth', route)
		def login():
		   ...
		   
		# Create route
		auth.new(url='/login', func=login, method='POST')
		
		# Instantiate all created routes
		auth.router()

'''
	def __init__(self, baseUrl, app, r=[]):
		self.baseUrl = self._url(baseUrl)
		self.app = app
		self.routes = r
		self.ordered = {}
		invalids = ("callback", "func")

		self.vars = [x for x in self.app.route.__code__.co_varnames[2:] if x not in invalids]

	def start(self):
		self.order(self.routes)
		self.make_mounts()

	def _url(self, x):
		if len(x) >= 1 and x[0] != '/':
			x = f'/{x}'
		while '//' in x:
			x = str(x).replace('//', '/')
		else:
			return x
	
	def make(self, routes):
		if len(routes) < 0:return {}
		al = {}
		for i, x in enumerate(self.vars):
			try:al[x] = routes[i]
			except IndexError:break
		return al

	def error(self, code, func):
		self.app.error(code, callback=func)

	def _route(self, url='', func=None, **kwargs):
		url = self._url(self.baseUrl+url)
		return self.app.route(url, **kwargs)(func)

	def route(self, url='', **kwargs):
		url = self._url(self.baseUrl+url)
		return self.app.route(url, **kwargs)

	def new(self, **config):
		route = {x: config[x] for x in config}
		self.routes.append(route)

	def mnt(self, url):
		self.baseUrl = self._url(url)

	def make_mounts(self):
		mounts = _get(self.routes, "mount")

		def _url(url):
			url = str(url)
			if not url.startswith("/"):url = "/"+url
			if not url.endswith("/"):url = url+"/"
			return url

		if not mounts:return
		for x in mounts:
			if "::" in mounts[x]:
				app, framework = mounts[x].split("::")
			else:
				app = mounts[x]
				framework = "bottle"
			app = get_app(app, framework)
			if framework == "bottle":
				self.order(app.urls.routes, x)
			self.app.mount(x, app)
		
	def router_v2(self, config=[]):
		routes = config if config != [] else self.routes
		def make(routes, base_url=''):
			for x in routes:
				if type(x) is str:
					base_url = base_url + self._url(x)
				elif type(x) is dict:
					path = _get(data=x, index='url')
					func = _get(data=x, index='func')
					url=base_url+self._url(path)
					decorators =  _get(x, "decorators")
					if decorators and type(decorators) is set:
						oths = self.make(x[2:-1])
						for decorator in decorators:
							func = decorator(func)
					else:oths = self.make(x[2:])
					self._route(url, func=func, **oths)
				elif type(x) is tuple:
					make(x[1], x[0])
				elif type(x) is list:
					make(x, base_url=base_url)
		make(routes)

	def find_route(self, name, routes=[]):
		routes = routes if routes != [] else self.ordered
		return routes[name]

	def order(self, routes={}, url=""):
		routes = routes if routes != [] else self.routes
		def make(routes, base_url):
			for x in routes:
				if type(routes[x]) is tuple:
					name = _get(routes[x], 2)
					if name:
						try:self.ordered[name] = str(base_url + x)
						except:pass

				elif type(routes[x]) is dict:
					make(routes[x], base_url=base_url+x)
				else:pass
		make(routes, base_url=url)
	
	def router(self, config=[]):
		routes = config if config != [] else self.routes
		def make(routes, base_url=''):
			for x in routes:
				if type(x) is int:
					func = _get(routes[x], 0)
					self.error(int(x), func)
				elif type(routes[x]) is list:
					make(routes[x], x)
				elif type(routes[x]) is tuple:
					func = _get(data=routes[x], index=0)
					url = base_url+self._url(x)
					decorators =  _get(routes[x], -1)

					name = _get(routes[x], 2)
					if name:
						try:self.ordered[name] = str(base_url + x)
						except:pass

					if decorators and type(decorators) is set:
						oths = self.make(routes[x][1:-1])
						for decorator in decorators:func = decorator(func)
					else:oths = self.make(routes[x][1:])
					self._route(url, func=func, **oths)

				elif type(routes[x]) is dict:
					make(routes[x], base_url=base_url+x)
				# elif type(routes[x]) is str:
				# 	if "::" in routes[x]:
				# 		app, framework = routes[x].split("::")
				# 	else:
				# 		app = routes[x]
				# 		framework = "bottle"
				# 	app = get_app(app, framework)
				# 	if framework == "bottle":
				# 		make(app.urls.routes, x)
						
				# 		return
				# 	else:self.app.mount(x, app)
		make(routes)

def get_app(appn, framework):
	if framework == "bottle":
		app = load_module(f"{appn}:" + f"{appn}".title() + "App()")
		app.setup(subapp=True)
		return app
	elif framework == "django":
		app = load_module(f"{appn}.wsgi")
		return app.application
	elif framework == 'flask':
		if "." in appn:
			app, ins = appn.split(".")
		else:
			app = appn
			ins = "app"
		app = load_module(app)
		return getattr(getattr(app, ins), "wsgi_app")
	elif framework == "pyramid":
		if "." in appn:
			app, ins = appn.split(".")
		else:
			app = appn
			ins = "app"
		app = load_module(app)
		return getattr(app, ins)

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine

class SqlalchemyDatabase:
	def __init__(self, path=None, debug=False, initialize=True, **kwargs):
		self.debug = debug
		self.path = path
		
		if isinstance(_get(kwargs, "metadata"), MetaData):
			self.metadata = _get(kwargs, "metadata")
		else:self.metadata = MetaData()
		self.Model = declarative_base(metadata=self.metadata)

		if initialize:
			self.initialize(**kwargs)
	
	def __call__(*args, **kwargs):
		return Session(*args, **kwargs)

	def _debug(self, text):
		if self.debug:print("[DEBUG]", text)

	def initialize(self, **kwargs):
		eng = kwargs.pop("engine") if _get(kwargs, "engine") else None
		sess = kwargs.pop("session") if _get(kwargs, "session") else None

		if type(eng) is dict:self.engine = create_engine(**eng)
		elif isinstance(eng, Engine):self.engine = eng
		else:self.engine = create_engine(self.path, encoding="utf-8")

		if type(sess) is dict:self.session = Session(bind=self.engine, **sess)
		elif isinstance(sess, (Session, sessionmaker)):self.session = sess
		else:self.session = Session(bind=self.engine, autocommit=True)
		
		self.s = self.session
	
	def create(self):
		self.metadata.create_all(self.engine)
