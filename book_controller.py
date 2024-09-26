from flask import jsonify
from flask_restful import Resource

# Sample data - list of book objects
books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 3, "title": "Design Patterns", "author": "Erich Gamma"},
]

class BookList(Resource):
    def get(self):
        """
        Get the list of books
        ---
        responses:
          200:
            description: A list of books
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: The book ID
                  title:
                    type: string
                    description: The title of the book
                  author:
                    type: string
                    description: The author of the book
        """
        return jsonify(books)
