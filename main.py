# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Interact with Sensorpush API
# author            : Ian Ault
# email             : aulti@csp.edu
# date              : 12-02-2022
# version           : v1.0
# usage             : python main.py
# notes             :
# license           : MIT
# py version        : 3.11.0 (must run on 3.6 or higher)
#==============================================================================
import json
import time
import os
import sys
import getpass

import requests


# The base URL for the API.
BASE_URL: str = "https://api.sensorpush.com/api/v1"


def read_file(filename, encoding="utf8"):
	"""Read a json file and return the contents.

	Args:
		filename (str): The name of the file to read.
		encoding (str, optional): The encoding of the file. Defaults to "utf8".

	Returns:
		dict: The contents of the file.

	"""
	with open(filename, "r", encoding=encoding) as file:
		data = json.load(file)

	return data

def write_file(filename, data, encoding="utf8"):
	"""Write data to a json file.

	Args:
		filename (str): The name of the file to write to.
		data (dict): The data to write to the file.
		encoding (str, optional): The encoding of the file. Defaults to "utf8".

	"""
	with open(filename, "w", encoding=encoding) as file:
		json.dump(data, file, indent=4, sort_keys=True)


class Sensors:
	def __init__(self, login_data):
		"""Initialize the class.

		Args:
			login_data (dict): The login data.

		"""
		self.authorization_code = self.get_authorization(login_data).json().get("authorization", None)
		self.access_token = self.get_access_token().json().get("accesstoken", None)
		if not self.access_token:
			os.remove("login.json")
			raise Exception("Unable to get access token. Check your credentials.")
		if not self.authorization_code:
			os.remove("login.json")
			raise Exception("Unable to get authorization code. Check your credentials.")

	@staticmethod
	def get_authorization(login_data):
		"""Log in using a valid email/password to recieve an authorization
		code.

		Args:
			login_data (dict): The login data.

		Returns:
			requests.models.Response: The authorization code.

		"""
		headers = {
			"accept": "application/json",
			"Content-Type": "application/json",
		}
		response = requests.post(
			os.path.join(BASE_URL, "oauth/authorize"),
			json=login_data,
			headers=headers,
			timeout=30
		)

		return response

	def get_access_token(self):
		"""Request a temporary oauth access token. Use the result from the
		previous step for the authorization code in the body.

		Returns:
			requests.models.Response: The access token.

		"""
		headers = {
			"accept": "application/json",
			"Content-Type": "application/json"
		}
		response = requests.post(
			os.path.join(BASE_URL, "oauth/accesstoken"),
			json={"authorization": self.authorization_code},
			headers=headers,
			timeout=30
		)

		return response

	def get_sensors(self):
		"""Request a list of sensors. Add the header "Authorization: " using
		the access_token returned in the OAuth Access step.

		Returns:
			dict: The sensors.

		"""
		headers = {
			"accept": "application/json",
			"Authorization": self.access_token
		}
		response = requests.post(
			os.path.join(BASE_URL, "devices/sensors"),
			json={},
			headers=headers,
			timeout=30
		)

		return response

def main():
	"""Main function.

	"""
	if not os.path.exists("login.json"):
		login_data = {
			"email": input("Email: "),
			"password": getpass.getpass("Password: ")
		}
		write_file("login.json", login_data)
	else:
		login_data = read_file("login.json")

	sensors = Sensors(login_data)

	while True:
		try:
			sensor_data = sensors.get_sensors().json()
			print(json.dumps(sensor_data["338676.17677938954275464014"], indent=4, sort_keys=True))
			time.sleep(2)
			# os.system("clear")
		except Exception as e:
			print(f"Error:\n\t{e}")
			time.sleep(10)
			sensors = Sensors(login_data)
		except KeyboardInterrupt:
			print("Exiting program...")
			sys.exit(0)


if __name__ == "__main__":
	main()
