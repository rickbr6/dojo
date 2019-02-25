from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    result = request.form

    qty = int(result['strawberry']) + int(result['apple']) + int(result['blackberry']) + int(result['raspberry'])

    print(f"Charging customer {result['first_name']} {result['last_name']} for {qty} fruits.")

    return render_template("checkout.html", info=result, qty=qty)


@app.route('/fruits')
def fruits():
    fruit = [{'name': 'Apple', 'source': 'static/img/apple.png', 'alt': 'apple.png'},
             {'name': 'BlackBerry', 'source': 'static/img/blackberry.png', 'alt': 'blackberry.png'},
             {'name': 'Raspberry', 'source': 'static/img/raspberry.png', 'alt': 'raspberry.png'},
             {'name': 'Strawberry', 'source': 'static/img/strawberry.png', 'alt': 'strawberry.png'}
             ]

    return render_template("fruits.html", fruit_info=fruit)


if __name__ == "__main__":
    app.run(debug=True)
