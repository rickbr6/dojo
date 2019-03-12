from flask import Flask, render_template, redirect, request, session, flash, url_for
from mysqlconnection import connectToMySQL
import re


app = Flask(__name__)
app.secret_key = "The super secret key. Don't tell anybody!"

SCHEMA = "registration"
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


@app.route('/')
def index():
    return render_template("registration.html")


@app.route('/process', methods=['POST'])
def process():
    print("adding a new user")
    print(request.form)
    is_valid = True
    if len(request.form['first_name']) < 1:
        is_valid = False
        flash("Please enter a valid first name")

    if len(request.form['last_name']) < 1:
        is_valid = False
        flash("Please enter a valid last name")

    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("Please enter a valid email address")

    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please enter a valid password")

    if request.form['password'] != request.form['confirm_password']:
        is_valid = False
        flash("Password mis-match. Please re-enter your password")

    if is_valid:
        print("No errors. Adding user to db")

        mysql = connectToMySQL(SCHEMA)
        query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at, email) VALUES (%(fname)s, %(lname)s, %(pwd)s, NOW(), NOW(), %{email));"
        data = {
            'fname': request.form['first_name'],
            'lname': request.form['last_name'],
            'email': request.form['email'],
            'pwd': request.form['password']
        }
        user_id = mysql.query_db(query, data)
        flash("Registration successful!")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
