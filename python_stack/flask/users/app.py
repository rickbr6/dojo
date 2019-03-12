from flask import Flask, render_template, redirect, session, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "This is a super secret string that nobody would ever be able to guess"

SCHEMA = "users_app"


@app.route('/')
def index():

    error = ''
    try:
        if request.method == "GET":
            mysql = connectToMySQL(SCHEMA)
            query = mysql.query_db('SELECT * FROM users;')
            print(query)

            return render_template("users.html", users=query)
        # elif request.method == "POST":

    except Exception as e:
        #flash(e)
        return


@app.route('/users/new', methods=['GET'])
def add_new_user():
    return render_template("/new_user.html")


@app.route('/users/create', methods=['POST'])
def add_new_user_to_db():
    new_user_first_name = request.form['first_name']
    new_user_last_name = request.form['last_name']
    new_user_email = request.form['email']
    print("Adding a new user to the db")

    mysql = connectToMySQL('users_app')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
    data = {
        'fname': new_user_first_name,
        'lname': new_user_last_name,
        'email': new_user_email
    }

    user_id = mysql.query_db(query, data)

    return redirect(f"users/{user_id}")


@app.route('/users/<user_id>', methods=['GET'])
def show_user_info(user_id):
    mysql = connectToMySQL(SCHEMA)

    query = "SELECT * FROM users WHERE id = %(uid)s;"
    data = {'uid': user_id}

    user_data = mysql.query_db(query, data)
    fname = user_data[0]['first_name']
    lname = user_data[0]['last_name']
    full_name = f"{fname} {lname}"
    email = user_data[0]['email']
    cdate = user_data[0]['created_at']
    udate = user_data[0]['updated_at']

    print(f"***USER DATA: {user_data}")

    return render_template("/user_id.html", id=user_id, full_name=full_name, fname=fname, lname=lname, email=email, cdate=cdate, udate=udate)


@app.route('/users/<user_id>/edit', methods=['GET'])
def show_user_edit(user_id):
    mysql = connectToMySQL(SCHEMA)

    query = "SELECT * FROM users WHERE id = %(uid)s;"
    data = {'uid': user_id}

    user_data = mysql.query_db(query, data)
    print(user_data)
    user_fname = user_data[0]['first_name']
    user_lname = user_data[0]['last_name']
    user_email = user_data[0]['email']

    return render_template("user_id_edit.html", id=user_id, fname=user_fname, lname=user_lname, email=user_email)


@app.route('/users/<id>/update', methods=['POST'])
def update_user_by_id(id):
    edit_user_fname = request.form['first_name']
    edit_user_lname = request.form['last_name']
    edit_user_email = request.form['email']
    print(f"The request form shows: {request.form}")
    print(f"Updating user {id} with fname of {edit_user_fname}in the db")

    mysql = connectToMySQL('users_app')
    query = "UPDATE users SET first_name = %(fname)s, last_name=%(lname)s, email=%(email)s WHERE id = %(id)s;"
    data = {
        'id': id,
        'fname': edit_user_fname,
        'lname': edit_user_lname,
        'email': edit_user_email,
    }
    print(f"Sending UPDATE Message: {query}")
    updated_user = mysql.query_db(query, data)
    print(f"Updated user id {id}. Return value is: {updated_user}")
    return redirect(f"users/{id}")


@app.route('/users/<id>/destroy', methods=['GET'])
def delete_user(id):

    mysql = connectToMySQL('users_app')
    query = "DELETE FROM users WHERE id=%(id)s;"
    data = {'id': id}

    print(f"Destroying record for ID: {id}")
    delete_id = mysql.query_db(query, data)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
