from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/survey', methods=['POST'])
def process_survey():
    print('Processing survey')
    print(request.form)
    name_on_form = request.form('name')
    return render_template('submitted_info.html', the_name=name_on_form)


if __name__ == '__main__':
    app.run(debug=True)
