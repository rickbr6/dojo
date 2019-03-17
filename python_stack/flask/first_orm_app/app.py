from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first_orm_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    age = db.Column(db.Integer)
    email = db.Column(db.String(45))
    create_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "Users(first_name='%s', last_name='%s', age='%s', email='%s, create_at='%s', updated_at='%s' )"\
               % (self.first_name, self.last_name, self.age, self.email, self.create_at, self.updated_at)


@app.route('/', methods=['GET', 'POST'])
def index():

    all_users = Users.query.all()
    print(all_users)

    return render_template("index.html", users=all_users)


@app.route('/add_user', methods=['POST'])
def add_user():
    print(f"REQUEST: {request.form['first_name']}")

    new_user = Users(first_name=request.form['first_name'], last_name=request.form['last_name'],
                     email=request.form['email'])
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
