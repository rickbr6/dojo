from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        for v in nums:
            num += v
        self.result += num
        return self

    def subtract(self, num, *nums):
        for v in nums:
            num -= v
        self.result -= num
        return self


md = MathDojo()

# x = md.add(2)
# print(f"RESULT: {x.result}")
#
# x = md.add(2, 5, 1)
# print(f"RESULT: {x.result}")
#
# x = md.subtract(3, 2)
# print(f"RESULT: {x.result}")

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)


if __name__ == '__main__':
    app.run(debug=True)
