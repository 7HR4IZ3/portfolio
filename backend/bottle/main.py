#pylint:disable=E1101
__get__ = ["app"]

from functools import partial
import random
from bottle import *
from threading import Thread
from http.server import SimpleHTTPRequestHandler, test
from session import SessionPlugin
from models import *

import json

app = Bottle()
app.install(DBPlugin(db))

# session = SessionPlugin()
# app.install(session)

# demo()

# Helper Functions
@app.hook("before_request")
def _():
	request.environ["PATH_INFO"] = request.environ["PATH_INFO"].rstrip("/")
	response.set_header("Access-Control-Allow-Origin", "*")
	response.set_header("Content-Type", "application/json")

# Application Views
@app.route("/api/<table>")
def index(table):
	data = table.get()
	if request.GET.keyword:
		data = table.like(sep="or", title="%"+str(request.GET.keyword).strip().replace(" ", "%")+"%", body="%"+request.GET.keyword+"%")
	elif request.GET.title:
		data = table.get(title=request.GET.title)
		if isinstance(data, db.List):
			return json.dumps(data, indent=4)
	length = len(data)
	if request.GET.get('from') and request.GET.get('to'):
		data = data[int(request.GET['from']) -1:int(request.GET.to)]
	if request.GET.limit:
		data = data[:int(request.GET.limit)]
	return json.dumps({"data": data, "total": length, "length": len(data)}, indent=4)

@app.route("/api/<table>/<idz:int>")
@app.route("/api/<table>/<idz:int>/<field>")
def get_id(idz, table, field=None):
	if request.method == "GET":
		data = (table.id==idz)
		if field:
			data = table.get(field, id==idz)
			if data == []:
				json.dumps({"status": "bad", "body": "No such column"}, indent=4)
		return data.json()
	elif request.method == "POST":
		try:
			table.new(request.POST)
			return json.dumps({"status": "ok"}, indent=4)
		except:
			return json.dumps({"status": "bad"}, indent=4)
	elif request.method == "PUT":
		try:
			table.set(request.PUT, id=idz)
			return json.dumps({"status": "ok"}, indent=4)
		except:
			return json.dumps({"status": "bad"}, indent=4)
	elif request.method == "DELETE":
		try:
			table.delete(id=idz)
			return json.dumps({"status": "ok"}, indent=4)
		except:
			return json.dumps({"status": "bad"}, indent=4)

@app.route("/api/<table>/length")
def index(table):
	data = table.get()
	return str(len(data))

@app.route("/api/<table>/random/<limit>")
def index(table, limit):
	data = table.get()
	ret = db.List()

	i = 0
	while i < int(limit):
		index = random.randint(0, len(data)) - 1
		ret.append(data[index])
		i += 1
	
	return ret.json()

@app.route("/api/<table>/new")
def new(table):

	try:
		table.new(request.POST)
		return json.dumps({"status": "ok"}, indent=4)
	except:
		return json.dumps({"status": "bad"}, indent=4)


@app.route("/api/commit")
def commit():
	try:
		return json.dumps({"status": "ok"}, indent=4)
	except:
		return json.dumps({"status": "bad"}, indent=4)

def run():
	Thread(target=app.run, kwargs={"port": 9999}).start()
	print()
	Thread(target=test, kwargs={"HandlerClass": partial(SimpleHTTPRequestHandler, directory=os.getcwd())}).start()

run()