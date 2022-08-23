import json
import os
import pickle
import re
import tempfile
from hashlib import sha1
from random import random
from time import time

def _urandom():
	if hasattr(os, "urandom"):
		return os.urandom(30)
	return str(random()).encode("ascii")

class BaseSessionStore(object):
	"""Base class for all session stores.
	:param session_class: The session class to use.
	"""

	def __init__(self, session_class=None):
		self.session_class = session_class

	def is_valid_key(self, key):
		"""Check if a key has the correct format."""
		return re.compile(r"^[a-f0-9]{40}$").match(key) is not None

	def generate_key(self, salt=None):
		"""Simple function that generates a new session key."""
		if salt is None:
			salt = repr(salt).encode("ascii")
		return sha1(b"".join([salt, str(time()).encode("ascii"), _urandom()])).hexdigest()

	def new(self):
		"""Generate a new session."""
		return self.session_class({}, self.generate_key(), True)

	def save(self, session):
		"""Save a session."""

	def save_if_modified(self, session):
		"""Save if a session class wants an update."""
		if session.should_save:
			self.save(session)

	def delete(self, session):
		"""Delete a session."""

	def get(self, sid):
		"""Get a session for this sid or a new session object. This
		method has to check if the session key is valid and create a new
		session if that wasn't the case.
		"""
		return self.session_class({}, sid, True)


# Used for temporary files by the filesystem session store.
_fs_transaction_suffix = ".__session"


class FilesystemSessionStore(BaseSessionStore):
	"""Simple example session store that saves sessions on the
	filesystem.

	:param path: The path to the folder used for storing the sessions.
		If not provided the default temporary directory is used.
	:param filename_template: A string template used to give the session
		a filename. ``%s`` is replaced with the session id.
	:param session_class: The session class to use.
	:param renew_missing: Set to ``True`` if you want the store to give
		the user a new sid if the session was not yet saved.

	.. versionchanged:: 0.1.0
		``filename_template`` defaults to ``secure_cookie_%s.session``
		instead of ``werkzeug_%s.sess``.
	"""

	def __init__(
		self,
		path=None,
		filename_template="secure_cookie_%s.session",
		session_class=None,
		renew_missing=False,
		mode=0o644,
	):
		super(FilesystemSessionStore, self).__init__(session_class=session_class)

		if path is None:
			path = tempfile.gettempdir()

		self.path = path

		assert not filename_template.endswith(_fs_transaction_suffix), (
			"filename templates may not end with %s" % _fs_transaction_suffix
		)
		self.filename_template = filename_template
		self.renew_missing = renew_missing
		self.mode = mode

	def get_session_filename(self, sid):
		# Out of the box this should be a strict ASCII subset, but you
		# might reconfigure the session object to have a more arbitrary
		# string.
		return os.path.join(self.path, self.filename_template % sid)

	def save(self, session):
		fn = self.get_session_filename(session.sid)
		fd, tmp = tempfile.mkstemp(suffix=_fs_transaction_suffix, dir=self.path)
		f = os.fdopen(fd, "wb")

		try:
			pickle.dump(dict(session), f, pickle.HIGHEST_PROTOCOL)
		finally:
			f.close()

		try:
			os.rename(tmp, fn)
			os.chmod(fn, self.mode)
		except (IOError, OSError):  # noqa: B014
			pass

	def delete(self, session):
		fn = self.get_session_filename(session.sid)

		try:
			os.unlink(fn)
		except OSError:
			pass

	def get(self, sid):
		if not self.is_valid_key(sid):
			return self.new()

		try:
			f = open(self.get_session_filename(sid), "rb")
		except IOError:
			if self.renew_missing:
				return self.new()
			data = {}
		else:
			try:
				try:
					data = pickle.load(f)
				except Exception:
					data = {}
			finally:
				f.close()

		return self.session_class(data, sid, False)

	def list(self):
		"""List all sessions in the store."""
		before, after = self.filename_template.split("%s", 1)
		filename_re = re.compile(
			r"{}(.{{5,}}){}$".format(re.escape(before), re.escape(after))
		)
		result = []
		for filename in os.listdir(self.path):
			# this is a session that is still being saved.
			if filename.endswith(_fs_transaction_suffix):
				continue
			match = filename_re.match(filename)
			if match is not None:
				result.append(match.group(1))
		return result