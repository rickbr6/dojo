from flask import Flask, render_template, redirect, request, session, flash, url_for
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "The super secret key. Don't tell anybody!"

bcrypt = Bcrypt(app)


SCHEMA = "registration"
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


@app.route('/')
def index():
    return render_template("registration.html")


@app.route('/process', methods=['POST'])
def process():
    print("adding a new user")
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
        pwd_hash = bcrypt.generate_password_hash(request.form['password'])

        mysql = connectToMySQL(SCHEMA)
        query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at, email) VALUES (%(fname)s, %(lname)s, %(pwd)s, NOW(), NOW(), %(email)s);"
        data = {
            'fname': request.form['first_name'],
            'lname': request.form['last_name'],
            'pwd': pwd_hash,
            'email': request.form['email']
        }

        user_id = mysql.query_db(query, data)
        flash("Registration successful!")
        return render_template("success.html", fname=request.form['first_name'])

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("Logging in")
        login_email = request.form['login_email']
        pwd_hash = bcrypt.generate_password_hash(request.form['user_pwd'])

        query = "SELECT * FROM users WHERE email=%(email)s;"
        data = {'email': login_email}

        mysql = connectToMySQL(SCHEMA)
        user_info = mysql.query_db(query, data)
        print(f"USER INFO: {user_info}")
        print(f"HASH: {pwd_hash}")
        if user_info:
            if bcrypt.check_password_hash(user_info[0]['password'], pwd_hash):
                print("Login Successful!")
            else:
                flash("Bad password")
        else:
            flash("Unknown user")

        return render_template("success.html", fname=user_info[0]['first_name'])


if __name__ == '__main__':
    app.run(debug=True)
