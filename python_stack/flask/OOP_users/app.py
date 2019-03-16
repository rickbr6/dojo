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
        self.account = BankAccount()

    def make_deposit(self, amount):
        print(f"Depositing ${amount} into account for User {self.first_name} {self.last_name}")
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        print(f"Withdrawal of ${amount} for User {self.first_name} {self.last_name}")
        self.account.make_withdrawal(amount)
        return self

    def display_user_balance(self):
        print(f"Balance for User {self.first_name} {self.last_name} is ${self.account.balance}")
        return self.account.display_balance()

    def transfer_money(self, to_user, amount):
        self.account.make_withdrawal(amount)
        to_user.account.deposit(amount)
        print(f"Transfer of ${amount} from {self.first_name} {self.last_name} to {to_user.first_name} {to_user.last_name}"
              f" complete")
        return self


class BankAccount:
    def __init__(self, int_rate=.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} complete")
        return self

    def make_withdrawal(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} complete")
        else:
            print(f"Insufficient funds (CurrentBalance: ${self.balance}). Charging a $5.00 fee")
            self.balance -= 5

    def display_balance(self):
        return self.balance


guido = User('Guido', 'Van Rossum', 'guido@email.com')
monty = User('Monty', 'Python', 'monty@email.com')
rick = User('Rick', 'Brown', 'rickbr@email.com')


guido.make_deposit(500).display_user_balance()
guido.transfer_money(rick, 150).display_user_balance()
rick.display_user_balance()


if __name__ == '__main__':
    app.run(debug=True)

