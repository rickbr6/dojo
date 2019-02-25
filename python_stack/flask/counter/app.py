from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"


@app.route('/', methods=['POST', 'GET'])
def index():

    if 'count' in session:
        print('key exists!')
        session['count'] = str(int(session['count']) + 1)
    else:
        print("Key 'key_name' does NOT exist")
        session['count'] = '1'

    print(session['count'])
    return render_template("index.html")


@app.route('/clear')
def reset_session():
    session.clear()
    return redirect('/')


@app.route('/add_two_sessions')
def add_two_sessions():
    session['count'] = str(int(session['count']) + 1)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
