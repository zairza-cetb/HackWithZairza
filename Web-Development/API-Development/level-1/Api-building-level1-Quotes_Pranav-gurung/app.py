from flask import Flask, jsonify, request
import random
from flask_smorest import abort
from db import quotes  # quotes should be a list of dicts

app = Flask(__name__)


def get_next_id():
    """Generate the next quote ID."""
    return max([q["id"] for q in quotes]) + 1 if quotes else 1


@app.get("/api/quotes")
def get_all_quotes():
    return jsonify(quotes), 200


@app.get("/api/quotes/random")
def get_random_quote():
    if not quotes:
        abort(404, message="No quotes available.")
    return jsonify(random.choice(quotes)), 200

@app.get("/api/quotes/category/<string:category>")
def get_quotes_by_category(category):
    filtered = [q for q in quotes if q["category"].lower() == category.lower()]
    if not filtered:
        abort(404, message="No quotes found for this category.")
    return jsonify(filtered), 200


@app.get("/api/categories")
def get_categories():
    categories = list(set(q["category"] for q in quotes))
    return jsonify(categories), 200


@app.get("/api/authors")
def get_authors():
    authors = list(set(q["author"] for q in quotes))
    return jsonify(authors), 200

@app.post("/api/quotes")
def add_new_quote():
    quote_data = request.get_json()
    if not quote_data or "text" not in quote_data or "author" not in quote_data or "category" not in quote_data:
        abort(400, message="Invalid data. Ensure 'text', 'author', and 'category' are included.")
    
    new_quote = {**quote_data, "id": get_next_id()}
    quotes.append(new_quote)
    return jsonify(new_quote), 201


@app.put("/api/quotes/<int:quote_id>")
def update_quote(quote_id):
    quote_data = request.get_json()
    if not quote_data or "text" not in quote_data or "author" not in quote_data or "category" not in quote_data:
        abort(400, message="Bad request. Ensure 'text', 'author', and 'category' are included.")
    
    for q in quotes:
        if q["id"] == quote_id:
            q.update(quote_data)
            return jsonify(q), 200
    
    abort(404, message="Quote not found.")

@app.delete("/api/quotes/<int:quote_id>")
def delete_quote(quote_id):
    for i, q in enumerate(quotes):
        if q["id"] == quote_id:
            deleted = quotes.pop(i)
            return jsonify({"message": "Quote deleted", "deleted": deleted}), 200
    
    abort(404, message="Quote not found.")


if __name__ == "__main__":
    app.run(debug=True)









