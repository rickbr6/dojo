from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


authors_of_books = db.Table('authors_of_books',
                         db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
                         db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True))


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    description = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    authors_of_this_book = db.relationship('Authors', secondary=authors_of_books)

    def __repr__(self):
        return "Books(book_id='%s', title='%s', description='%s', created_at='%s', updated_at='%s')" % \
               (self.id, self.title, self.description, self.created_at, self.updated_at)


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    notes = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    books_by_this_author = db.relationship('Books', secondary=authors_of_books)

    def __repr__(self):
        return "Authors(author_id='%s', first_name='%s', last_name='%s', notes='%s', created_at='%s', updated_at='%s')"\
               % (self.id, self.first_name, self.last_name, self.notes, self.created_at, self.updated_at)


@app.route('/', methods=['GET', 'POST'])
def index():

    all_books = Books.query.all()

    return render_template("index.html", books=all_books)


@app.route('/authors', methods=['GET', 'POST'])
def show_authors():
    print(f"REQUEST FORM FOR SHOW AUTHORS: {request.form}")
    all_authors = Authors.query.all()

    return render_template("authors.html", authors=all_authors)


@app.route('/add_book', methods=['POST'])
def add_book():
    print(f"REQUEST FORM FOR ADD BOOK: {request.form}")

    new_book = Books(title=request.form['title'], description=request.form['description'])
    db.session.add(new_book)
    db.session.commit()

    return redirect("/")


@app.route('/add_author', methods=['POST'])
def add_author():
    print(f"REQUEST FORM FOR ADD AUTHOR: {request.form}")

    new_author = Authors(first_name=request.form['first_name'], last_name=request.form['last_name'],
                         notes=request.form['notes'])

    db.session.add(new_author)
    db.session.commit()

    return redirect("/authors.html")


@app.route('/books/<id>', methods=['GET'])
def show_book_info(id):

    current_book = Books.query.get(id)
    print(current_book)

    authors = current_book.authors_of_this_book

    return render_template("books.html", title=current_book.title, id=current_book.id,
                           description=current_book.description, authors=authors)


@app.route('/author/<id>', methods=['GET'])
def show_author_info(id):

    current_author = Authors.query.get(id)
    print(current_author)

    books = current_author.books_by_this_author
    print(f"Viewing current author: {current_author}")
    print(f"Books by this author are: {books}")

    return render_template("author_bio.html", first_name=current_author.first_name, last_name=current_author.last_name,
                           notes=current_author.notes, books=books)


if __name__ == '__main__':
    app.run(debug=True)
