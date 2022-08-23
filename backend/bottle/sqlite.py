import json, re
import sqlite3

def makelist(data):  # This is just too handy
	if isinstance(data, (tuple, list, set, dict)):
		return list(data)
	elif data:
		return [data]
	else:
		return []

class Hooks:
	__hooks = {}

	def on(self, event, func=None, override=False):
		def wrap(func):
			funcs = makelist(func or [])
			if event not in self._:
				self.__hooks[event] = funcs
			else:
				self.__hooks[event] += funcs
		return wrap(func) if func else wrap 

	def trigger(self, event, *args, **kwargs):
		if event in self.__hooks:
			for func in self.__hooks[event]:
				if callable(func):
					func(*args, **kwargs)
	
	def remove(self, event):
		if event in self.__hooks:
			self.__hooks.pop(event)
	
	def detach(self, event, func):
		if event in self.__hooks and func in self.__hooks[event]:
			self.__hooks[event].remove(func)

class SqliteDatabase(Hooks):
	def __init__(self, path, debug=False, verbose=False, initialize=True, **kwargs):
		self.debug = debug
		self.path = path
		
		self.Model = Model
		self.Model.db = self
		self.Column = Column
		self.List = List
		
		self.models = {}
		self.verbose = verbose
		self.kw = kwargs

		if initialize:
			self.connect()

	def _debug(self, *text):
		if self.debug:print("[DEBUG]", *text)

	def _debug_(self, *text):
		if self.verbose:print("[VERBOSE]", *text)

	def connect(self):
		try:
			self._debug('[+] Connecting To Database %s' %self.path)
			self.connection = sqlite3.connect(self.path, **self.kw)
			self.connection.row_factory = sqlite3.Row
			self.cursor = self.connection.cursor()
			self.trigger("connect")
			self._debug('[+] Connected Successfully To %s \n' %self.path)
			return True
		except Exception as e:
			self._debug(f'[-] An Error Occured: .. Try Again \n')
			self._debug('[INFO]', e)
			self.trigger("error", e)
			return False

	def _tables(self):
		self.cursor.execute(
			"SELECT * FROM sqlite_master WHERE type='table'"
		)
		tables = self.cursor.fetchall()
		return [x[1] for x in tables]

	def _columns_(self, table, as_str=False):
		data = self.execute(f"SELECT sql FROM sqlite_master where type='table' AND name NOT LIKE 'sqlite_%' AND name='{table}'", one=True, serialize=False)
		ret = {}
		if data:
			data = data[0].split("(")[1].split(")")[0].split(",")
			for x in data:
				x = x.strip().split(" ")
				ret[x[0].replace('"', "")] = x[1]
		else:
			data = self.execute(f"SELECT sql FROM sqlite_master where type='table' AND name NOT LIKE 'sqlite_%'")
			self._debug(data)

		return ret if as_str == False else [x for x in ret]
	 
	def table(self, table, data=None):
		try:
			if table not in self._tables():
				self._debug('[+] Creating Database Table "%s"' %table)
				if data:
					# Data syntax
					# 
					
					columns = ",".join(data[x]._query() for x in data)					
					query = "CREATE TABLE IF NOT EXISTS %(table)s (%(columns)s)"%{
						'table': table,
						'columns': columns
					}

					self.execute(query)
					self.connection.commit()
					self._debug('[+] Database Table Sucessfully Created \n')
			else:
				self._debug('[-] Table Already Exists')
		except Exception as e:
			self._debug(f'[-] Database Table Could Not Be Created Or Already Exists \n')
			self._debug('[INFO]', e)
			self.trigger("error", e)

	def add_column(self, table, data=None, default=None):
		try:
			if table in self._tables():
				self._debug('[+] Altering Database Table "%s"' %table)
				if data:
					# Data syntax
					# {'id': 'INTEGER PRIMARY KEY', 'name': 'text', 'email': 'text'}
					for x in data:
						d = "DEFAULT ?" if default.get(x) else ""
						self.execute(f'ALTER TABLE {table} ADD COLUMN "{x}" ?', args=[data[x], default.get(x)] if x in default else [data[x]])
					self._debug('[+] Database Table Sucessfully Altered \n')
			else:
				self._debug('[-] Table Does Not Exists')
		except Exception as e:
			self._debug('[-] Database Table Could Not Be Altered Or Does Not Exists \n')
			self._debug('[INFO]', e)
			self.trigger("error", e)
	
	def drop_column(self, table, columns):
		try:
			if table in self._tables():
				self._debug('[+] Altering Database Table "%s"' %table)
				if columns:
					# Data syntax
					# {'id', 'name', 'email'}
					if type(columns) is str:
						self.execute(f"ALTER TABLE {table} DROP COLUMN {columns}")
					else:
						for x in columns:
							self.execute(f"ALTER TABLE {table} DROP COLUMN {x}")
					self.connection.commit()
					self._debug('[+] Database Table Column Sucessfully Dropped \n')
			else:
				self._debug('[-] Table Does Not Exists')
		except Exception as e:
			self._debug('[-] Database Table Column Could Not Be Droped Or Does Not Exists \n')
			self._debug('[INFO]', e)
			self.trigger("error", e)

	def create(self, table, data=None):
		try:
			self._debug('[+]Inserting Data To Database Table "%s"' %table)
			if data:
				# Data syntax
				# ('test', 'test@test.com')
				columns = List(data.keys())
				
				query = "INSERT INTO %(table)s (%(columns)s) VALUES (%(qmarks)s)" %{
					'table': table,
					'columns': ','.join(columns),
					'qmarks': str('?, ' * len(columns))[:-2]
				}
				self.execute(query, args=List(data.values()))
	
				self.connection.commit()
				self._debug('[+] Data Sucessfully Inserted \n')
		except Exception as e:
			self._debug('[+] An Error Occured \n')
			self._debug('[INFO]', e)
			self.trigger("error", e)

	def read(self, table, *select, as_json=False, **where):
		try:
			if not select:
				select = ("*",)
			if where:
				values = List(where.values())
				where = "WHERE " +  "".join(f"{x} = ? AND " for x in where)[:-5]
			else:
				where = ''
				values = []
			query = "SELECT %(select)s FROM %(table)s %(where)s" % {
					'select': ','.join(select),
					'table': table,
					'where': where
				}

			data = self.execute(query, args=values)
			if as_json:
				data = json.dumps(data)
				self._debug('[+] Returning as json')
			self._debug('[+] Read From Table "%s" Successful' %table)
			return data
		except Exception as e:
			self._debug('[-] Could Not Read From Table "%s" .. The table Might Not Exist' %table)
			self._debug('[INFO]', e)
			self.trigger("error", e)

	def update(self, table, _data=None, **where):
		try:
			self._debug('[+] Updating Data To Database Table "{}" Where "{}"'.format(table, where))
			update = _data or {}
			if update:
				# Data syntax
				# name = ?, email = ?, ('example', 'example@gmail.com')
				values = List(update.values())
				update = "".join(f"{x} = ?, " for x in update)[:-2]
				
				if where:
					values += List(where.values())
					where = "WHERE " +  "".join(f"{x} = ? AND " for x in where)[:-5]
				else:
					where = ''
				
				query = "UPDATE %(table)s SET %(update)s %(where)s" %{
					'table': table,
					'update': update,
					'where': where
				}
				self.execute(query, args=values)
				
				self.connection.commit()
				self._debug('[+] Data Updated')
		except Exception as e:
			self._debug('[-] Could Not Update Data In Table "%s" .. The table Might Not Exist' %table)
			self._debug('[INFO]', e)
			self.trigger("error", e)

	def delete(self, table, where=None):
		try:
			if where:
				values = List(where.values())
				where = "WHERE " "".join(f"{x} = ? AND " for x in where)[:-5]
				
				query = f"DELETE FROM %(table)s %(where)s"%{
					'table': table,
					'where': where
				}
				
				self.execute(query, args=values)
				self.connection.commit()
			else:
				self.execute(f"DELETE FROM %s"%table)
				self.connection.commit()
			return True
		except Exception as e:
			self._debug('[INFO]', e)
			self.trigger("error", e)
			return False

	def execute(self, query, args=None, one=False, serialize=True):
		#try:
		self._debug('[+] Running Query ')
		self.trigger("query", query, args=args)
		if args:
			self.cursor.execute(query, args)
		else:
			self.cursor.execute(query)
		
		self._debug_('[QUERY]', str(query), args or '')

		data = self.cursor.fetchone() if one else self.cursor.fetchall()
		if serialize:
			data = self.serialize(data)
		self._debug_('[RESPONSE]', data)
		self.connection.commit()
		self._debug('[+] Query Successfully Executed \n')
		return data
		#except :
#			self._debug('[-] An Error Occured.. Check The Query \n')
#			raise e
	
	def execute_many(self, query, serialize=True):
		try:
			self._debug('[+] Running Query ')
			self.cursor.executescript(str(query))
			data = self.cursor.fetchall()
			if serialize:
				data = self.serialize(data)
			self.connection.commit()
			self._debug('[+] Query Successfully Executed \n')
			return data
		except Exception as e:
			self._debug('[-] An Error Occured.. Check The Query \n') 
		
	def serialize(self, data):
		try:
			dic = List()

			def wrap(row):
				d = {key: val for key, val in zip(row.keys(), row)}
				dic.append(d)

			if isinstance(data, list):
				for row in data:
					wrap(row)
			elif isinstance(data, sqlite3.Row):
				wrap(data)
	
			return dic
		except Exception as e:
			pass
	
	def drop(self, table):
		self.execute(f"DROP {table}")
		self.connection.commit()

	def init(self, *models):
		for model in models:
			model.db = self
			model().create()
			self.trigger("init_model", model)
		return

	def __del__(self):
		self.connection.close()

class List(list):
	def __or__(self, other):
		return List(set([*self, *other]))
	
	def __and__(self, other):
		if self == other:
			return self
		alll = List()
		if self:
			for x in self:
				if other and x in other:
					alll.append(x)
		elif other:
			alll = other
		return alll
	
	def json(self):
		return json.dumps(self, indent=4)

class Column:
	def __init__(self, type="text", null=True, default=False, primary_key=False, unique=False):
		self.type = type
		self.null = null
		self.default = default
		self.unique = unique
		self.pk = primary_key
		
		self._table = None
	
	def _dtype(self):
		null = ' NOT NULL' if not self.null else ''
		default = f' DEFAULT {self.default}' if self.default else ''
		unique = " UNIQUE" if self.unique else ""
		type = f'{self.type} primary key' if self.pk else self.type
		
		return f'{type}{null}{default}{unique}'
	
	def _query(self):
		q = f'"{self.name}" {self._dtype()}'
		return q
	
	def __eq__(self, other):
		data = self._table.get(**{self.name: other})
		return List(data)

	def contains(self, word):
		ret = List()
		for x in self._table.get():
			if word in x[self.name]:
				ret.append(x)
		return ret
	
	def match(self, value: str):
		ret = List()
		for x in self._table.get():
			if re.search(value, x[self.name]):
				ret.append(x)
		return ret
	
	def like(self, word):
		data = self._table.like(self._name, word)
		return List(data)

	def __lt__(self, value):
		ret = List()
		for x in self._table.get():
			if x[self.name] < value:
				ret.append(x)
		return ret

	def __gt__(self, value):
		ret = List()
		for x in self._table.get():
			if x[self.name] > value:
				ret.append(x)
		return ret

	def __le__(self, value):
		return List(
			[*self.__lt__(value), *self.__eq__(value)]
		)

	def __ge__(self, value):
		return List(
			[*self.__gt__(value), *self.__eq__(value)]
		)

class Model:
	def __init__(self):
		self._name = self.__class__.__name__

		invalids = ['create', 'delete', 'new', 'get', 'set', 'like', "update"]
		self.columns = {}
		
		for x in dir(self):
			if not x.startswith('_') and isinstance(getattr(self, x), self.db.Column) and x not in invalids:
				column = getattr(self, x)
				column._table = self
				column.name = x
				self.columns[x] = column
		
		if "id" not in self.columns:
			self.id = self.db.Column("integer", primary_key=True, null=False)
			self.id._table = self
			self.id.name = "id"
			self.columns["id"] =self.id

	def __call__(self, *args, **kwds):
		return self.new(*args, **kwds)

	def _compare(self, old, new):
		added, removed= {}, {}
		if old == new:return {'added': added, 'removed': removed}
		for a in old:
			if a not in new:removed[a] = old[a]
		for b in new:
			if b not in old:added[b] = new[b]._dtype()
		return {'added': added, 'removed': removed}

	def create(self):
		self.db.models[self.__class__.__name__] = self
		if self._name not in self.db._tables():
			self.db.table(self._name, self.columns)
			return
		compare = self._compare(self.db._columns_(self._name), self.columns)
		if compare['added'] != {}:
			self.db.add_column(self._name, compare['added'])
			self.db._debug(f"Added: {compare['added']}")
		if compare['removed'] != {}:
			self.db.drop_column(self._name, compare['removed'])
			self.db._debug(f"Removed: {compare['removed']}")
	
	def like(self, sep="and", **data):
		l = "".join("%s like ? %s "%(x, sep) for x in data)[:-(2+len(sep))]
		query = "select * from %s where %s"%(self._name, l)
		data = self.db.execute(query, args=list(data.values()))
		return data

	def get(self, *select, as_json=False, **where):
		data = self.db.read(self._name, *select, as_json=as_json, **where)
		return data

	def set(self, _data, **where):
		data = self.db.update(self._name, _data, **where)
		return data
	
	def update(self, _data=None, **kw):
		return self.set(_data, **kw)

	def new(self, _data=None, **kw):
		data = _data or {}
		data = dict(**data, **kw)
		self.db.create(self._name, data)
		return True
	
	def delete(self, **where):
		return self.db.delete(self._name, where=where)
