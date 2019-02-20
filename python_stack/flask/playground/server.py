from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def play():
    return render_template('index.html')


@app.route('/play/<num>/<color>')
def display_boxes(num, color):
    return render_template("index.html", num_times=int(num), box_color=color)


if __name__ == "__main__":
    app.run(debug=True)

