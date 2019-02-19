from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/success')
def success():
    return "Success"


@app.route('/hello/<name>')  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name


@app.route('/users/<username>/<id>')  # for a route '/users/____/____', two parameters in the url get passed as
# username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":
    app.run(debug=True)
