from flask import Flask, render_template, redirect, session, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "This is a random string that nobody will ever guess!"


@app.route('/')
def index():
    mysql = connectToMySQL('pets')
    query = mysql.query_db('SELECT * FROM pets;')

    # print(query)
    return render_template('index.html', pets=query)


@app.route('/add_pet', methods=['POST'])
def add_pet():
    new_pet_name = request.form['name']
    new_pet_type = request.form['type']

    print(f"New Pet name = {new_pet_name}, pet type = {new_pet_type}")

    mysql = connectToMySQL('pets')

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"

    data = {
        'name': request.form['name'],
        'type': request.form['type'],
    }

    new_pet_id = mysql.query_db(query, data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

