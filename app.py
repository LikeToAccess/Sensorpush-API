# -*- coding: utf-8 -*-
# filename          : restful.py
# description       : API to grab movie links
# author            : Ian Ault
# email             : liketoaccess@protonmail.com
# date              : 05-24-2022
# version           : v1.0
# usage             : python restful.py
# notes             :
# license           : MIT
# py version        : 3.10.2 (must run on 3.6 or higher)
#==============================================================================
import base64
import os
import json

from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from waitress import serve
from flask import Flask

from settings import *
from sensorpush import Sensors, get_login_data


app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"*": {"origins": "*"}})
login_data = get_login_data()
sensors = Sensors(login_data)


class Sensorpush(Resource):
	def get(self):
		sensor_data = sensors.get_sensors().json()
		return {"message": "Okay", "data": sensor_data}, 200

	def put(self):
		return {"message": "Not implemented"}, 501

	def post(self):
		return {"message": "Not implemented"}, 501

class Test(Resource):
	def get(self):
		return {"message": "Not implemented"}, 501

	def post(self):
		return {"message": "Not implemented"}, 501


def main():
	api.add_resource(Test, "/test")
	api.add_resource(Sensorpush, "/api/v1/sensorpush")

	print(f"Starting server on port {PORT}...")

	if DEBUG_MODE:
		print("DEBUG: Running in debug mode")
		app.run(host=HOST, port=PORT, debug=True)
	else:
		serve(app, host=HOST, port=PORT)


if __name__ == "__main__":
	main()
