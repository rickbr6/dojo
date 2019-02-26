from flask import Flask, render_template, session, redirect, request
import random


app = Flask(__name__)
app.secret_key = "This is a test of the random kind"


@app.route('/')
def index():
    # session.clear()
    if 'random_num' in session:
        print(f"The current random number is: {session['random_num']}")
    else:
        session['random_num'] = random.randint(1, 100)
        session['count'] = '0'
        print(f"Generating new random number: {session['random_num']}")
        session['commentary'] = 'Take a guess'

    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def user_guess():

    number = request.form
    session['guess'] = number['user_guess']
    print(f"Guess:{session['guess']} Random:{session['random_num']}")

    # if int(session['guess']) ==
    print(type(int(session['guess'])))
    if int(session['guess']) > int(session['random_num']):
        print(f"The guess {session['guess']} is greater than the random number {session['random_num']}")
        session['count'] = str(int(session['count']) + 1)
        session['commentary'] = session['guess'] + " is too High!"

    elif int(session['guess']) < int(session['random_num']):
        print(f"The guess {session['guess']} is less than the random number {session['random_num']}")
        session['count'] = str(int(session['count']) + 1)
        session['commentary'] = session['guess'] + " is too Low!"

    elif int(session['guess']) == int(session['random_num']):
        print(f"The guess {session['guess']} is equal to random number. You win!")
        session['commentary'] = session['guess'] + " is Correct! You Won in only " + session['count'] + " tries!"
        session['count'] = '0'

    return redirect('/')


@app.route('/clear')
def clear_session():
    session.clear()
    session['count'] = '0'
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
