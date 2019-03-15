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
    print("In process function")
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

        print("Adding new user")
        print(request.form)

        mysql = connectToMySQL(SCHEMA)
        query = "INSERT INTO users (first_name, last_name, password, created_at, updated_at, email) VALUES (%(fname)s, %(lname)s, %(pwd)s, NOW(), NOW(), %(email)s);"
        data = {
            'fname': request.form['first_name'],
            'lname': request.form['last_name'],
            'pwd': pwd_hash,
            'email': request.form['email']
        }
        print(f'QUERY: {query}')
        user_id = mysql.query_db(query, data)
        flash("Registration successful!")
        return render_template("dashboard.html", fname=request.form['first_name'])

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("Logging in")
        login_email = request.form['login_email']
        print(f"LOGIN EMAIL: {login_email}")
        print(f"REQUEST.FORM: {request.form}")

        query = "SELECT * FROM users WHERE email=%(email)s;"
        data = {'email': login_email}

        mysql = connectToMySQL(SCHEMA)
        user_info = mysql.query_db(query, data)
        print(f"USER INFO: {user_info}")
        if user_info:
            if bcrypt.check_password_hash(user_info[0]['password'], request.form['user_pwd']):
                print("Login Successful!")
                session['id'] = user_info[0]['id']
                print(f"Added New session with ID: {session['id']}")
                # return render_template("dashboard.html", fname=user_info[0]['first_name'])
                return redirect('/dashboard')
            else:
                print(f"USER_INFO HASH: {user_info[0]['password']}")

                flash("Bad password")
        else:
            flash("Unknown user")

        return redirect('/')


@app.route('/dashboard', methods=['GET', 'POST'])
def show_dashboard():
    testvar = "test"
    if request.method == "GET":
        print("Rendering dashboard.html")

        # Get tweets:
        mysql = connectToMySQL(SCHEMA)
        query = "SELECT tweets.user_id, tweets.id, CONCAT_WS(' ', users.first_name, users.last_name) as full_name, users.created_at, users.updated_at," \
                " tweets.content FROM users JOIN tweets on users.id = tweets.user_id ORDER BY tweets.id desc"

        tweet_messages = mysql.query_db(query)

        print(f"TWEETS: {tweet_messages}")

        return render_template("dashboard.html", tweets=tweet_messages)



@app.route('/tweets/create', methods=['POST'])
def post_a_message():
    message = request.form['tweet']
    user_id = session['id']
    print(f"User with ID {user_id} posted the message: {message}")

    mysql = connectToMySQL(SCHEMA)
    query = "INSERT INTO tweets (id, user_id, content, created_at, updated_at) VALUES (%(uid)s, %(message)s, NOW(), NOW());"
    data = {
        'uid': user_id,
        'message': message
    }

    tweet_id = mysql.query_db(query, data)
    print("Posted message with ID {tweet_id} to tweet.db")
    print(session)

    # return render_template('dashboard.html', tweets=tweet_messages)
    return redirect('/dashboard')


@app.route('/logout', methods=['GET'])
def logout():
    print("Logging out user")
    if session.keys:
        print(f"Logging out user with id: {session['id']}")
        session.clear()
    return redirect(url_for('index'))


@app.route('/tweets/<tweet_id>/add_like', methods=['GET', 'POST'])
def add_like(tweet_id):
    mysql = connectToMySQL(SCHEMA)
    query = "INSERT INTO likes (tweet_id) VALUES (%(tweet_id)s);"
    data = {
        'tweet_id': tweet_id
    }
    like_id = mysql.query_db(query, data)

    print("Liked message with ID {tweet_id}. Message id: {like_id}")

    return redirect('/dashboard')


@app.route('/tweets/<tweet_id>/delete', methods=['GET', 'POST'])
def delete_post(tweet_id):
    mysql = connectToMySQL(SCHEMA)
    query = "DELETE FROM tweets WHERE (%(tweet_id)s) = id;"
    data = {
        'tweet_id': tweet_id
    }
    deleted = mysql.query_db(query, data)

    print('*'*40)
    print(f"Message with ID {tweet_id} has been deleted. DELETED = {deleted}")

    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)
