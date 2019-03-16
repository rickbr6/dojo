from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        print(f"Deposit of ${amount} for User {self.first_name} {self.last_name}")
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        print(f"Withdrawal of ${amount} for User {self.first_name} {self.last_name}")
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Balance for User {self.first_name} {self.last_name} is ${self.account_balance}")
        return self.account_balance

    def transfer_money(self, to_user, amount):
        self.make_withdrawal(amount)
        to_user.make_deposit(amount)

        print(f"Transfer of ${amount} from {self.first_name} {self.last_name} to {to_user.first_name} {to_user.last_name}"
              f" complete")

        return self


guido = User('Guido', 'Van Rossum', 'guido@email.com')
monty = User('Monty', 'Python', 'monty@email.com')
rick = User('Rick', 'Brown', 'rickbr@email.com')

guido.make_deposit(50).make_deposit(100).make_deposit(200).display_user_balance()
guido.make_withdrawal(50).display_user_balance()
guido.transfer_money(rick, 50).display_user_balance()
rick.display_user_balance()


if __name__ == '__main__':
    app.run(debug=True)

