from flask import Flask, render_template, redirect, request, session, flash, url_for
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "The super secret key. Don't tell anybody!"

SCHEMA = "registration"


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

    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please enter a valid password")

    if request.form['password'] != request.form['confirm_password']:
        is_valid = False
        flash("Password mis-match. Please re-enter your password")

    if is_valid:
        print("No errors. Adding user to db")

        mysql = connectToMySQL(SCHEMA)
        query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(pwd)s, NOW(), NOW());"
        data = {
            'fname': request.form['first_name'],
            'lname': request.form['last_name'],
            'pwd': request.form['password']
        }
        user_id = mysql.query_db(query, data)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
