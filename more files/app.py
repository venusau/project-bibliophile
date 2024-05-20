from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Book model for the database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cover_image = db.Column(db.String(100), nullable=False)
    donated = db.Column(db.Boolean, default=False)

@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_data = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "description": book.description,
            "coverImage": book.cover_image,
            "donated": book.donated
        }
        book_list.append(book_data)
    return jsonify(book_list)

@app.route('/api/books', methods=['POST'])
def add_book():
    new_book_data = request.json
    new_book = Book(
        title=new_book_data['title'],
        author=new_book_data['author'],
        genre=new_book_data['genre'],
        description=new_book_data['description'],
        cover_image=new_book_data['coverImage'],
        donated=new_book_data.get('donated', False)  # Set donated status if provided, default to False
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
