from flask import Flask, request, abort, jsonify, render_template, redirect, url_for

from forms import bookForm
from models import books


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/books/", methods=["GET"])
def books_list():
    return render_template("list.html", books=books.all())

@app.route("/books/new/", methods=["GET", "POST"])
def book_new():
    form = bookForm()

    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
        return redirect(url_for("books_list"))
    return render_template("form_new.html", form=form)

@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id)
    form = bookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id, form.data)
        return redirect(url_for("books_list"))
    return render_template("form_edit.html", form=form, book_id=book_id)

@app.route("/books/delete/<int:book_id>/", methods=["GET"])
def book_delete(book_id):
    result = books.delete(book_id)
    return redirect(url_for("books_list"))

    # form = bookForm(data=book)

    # if request.method == "POST":
    #     if form.validate_on_submit():
    #         books.update(book_id, form.data)
    #     return redirect(url_for("books_list"))
    # return render_template("form_edit.html", form=form, book_id=book_id)


@app.route("/api/v1/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    result = books.get(book_id)
    if not result:
        abort(404)

    return jsonify({'result': result})

@app.route("/api/v1/books/", methods=['GET'])
def get_books():
    result = books.all()
    if not result:
        abort(404)

    return jsonify({'result': result})

@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'title': request.json['title'],
        'writer': request.json['writer'],
        'date': request.json['date'],
    }
    books.create(book)
    return jsonify({'book': book}), 201

@app.route("/api/v1/books/", methods=["PUT"])
def update_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'title': request.json['title'],
        'writer': request.json['writer'],
        'date': request.json['date'],
    }
    books.update(request.json['id'], book)
    return jsonify({'book': book}), 201


@app.route("/api/v1/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
