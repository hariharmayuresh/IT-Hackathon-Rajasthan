import os

import mysql.connector as connection
conn = connection.connect(host = 'localhost', user = "root", password = "VM@152225@SM", use_pure = True, database = "login_info")
cur = conn.cursor()
# cur.execute("show databases")


import flask
from flask import Flask, render_template, redirect,jsonify, request, session

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('register.html')

@app.route('/submit', methods = ["POST"])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    password = str(request.form.get('pass'))
    cur.execute("use login_info")
    query = " INSERT INTO credentials values(%s, %s, %s)"
    val = [(name, email, password )]
    cur.executemany(query, val)
    conn.commit()
    return render_template("signin.html")

@app.route('/sign_in' , methods = ["POST"])
def sign_in():
    email = request.form.get('email')
    password = str(request.form.get('pass'))

    cur.execute("""SELECT * FROM `credentials` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email,password))
    cred=cur.fetchall()
    return redirect('/')

@app.route('/member')
def member():
    return render_template('signin.html')

@app.route('/register')
def resitration():
    return render_template('register.html')

@app.route('/land_holder')
def holder():
    return render_template('land_holder.html')

@app.route('/rental_person')
def rental():
    return render_template('rental_person.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == ('__main__'):
    app.run(debug=True)



# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
  land = request.form['land']
  price = request.form['price']
  # add land and price to database
  return 'Land and price added successfully'

@app.route('/rent', methods=['POST'])
def rent():
  land = request.form['land']
  duration = request.form['duration']
  # rent a person for farming for the specified duration
  return 'Person rented for farming successfully'

@app.route('/service', methods=['POST'])
def service():
  service = request.form['service']
  land = request.form['land']
  # provide the requested service for the specified land
  return 'Service provided successfully'

# if __name__ == '__main__':
#   app.run()