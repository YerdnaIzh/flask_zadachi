import sqlite3

class Database:
	def __init__(self):
		self.sqlite_connection = sqlite3.connect('primer.db')
		self.cursor = self.sqlite_connection.cursor()

	def add_user(self, user_ip):
		query = "INSERT INTO users (user_ip) VALUES (?)"
		self.cursor.execute(query, (user_ip,))
		self.sqlite_connection.commit()

	def add_task(self, user_ip, task):
		query = "INSERT INTO zadachi (user_ip, zadacha) VALUES (?, ?)"
		self.cursor.execute(query, (user_ip, task))
		self.sqlite_connection.commit()

	def close(self):
		self.sqlite_connection.close()
