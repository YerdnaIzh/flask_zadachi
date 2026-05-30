from flask import Flask, render_template, request, redirect

import db

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add_zadacha', methods=['POST', 'GET'])
def add_zadacha():
	if request.method == 'POST':
		zadacha = request.form['zadacha']
		ip_addr = request.remote_addr
		d = db.Database()
		d.add_task(ip_addr, zadacha)
		d.close()
		return redirect('/')
	else:
		return redirect('/')


app.run()