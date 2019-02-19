from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def hello_dojo():
    return 'Hello Dojo!'


@app.route('/repeat/<num>/<greeting>')
def hello(num, greeting):
    greeting = str((greeting + ' ') * int(num))
    return greeting + "!"


@app.route('/users/<username>/<id>')  # for a route '/users/____/____', two parameters in the url get passed as
# username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


@app.route('/<val>')
def default_route(val):
    return "Sorry! No Response. Please try again"


if __name__ == "__main__":
    app.run(debug=True)
