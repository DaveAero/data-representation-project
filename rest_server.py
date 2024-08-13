from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Database in memory for now
books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
    {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]
nextId=4


# at the root page of the server
@app.route('/')
# this index function will be run
def index():
    # This text is displated in the HTML browser
    return "hello"

# at the url /books
@app.route('/books')
def getAll():
    # this is displayed in the HTML browser
    return jsonify(books)

# Find by id
@app.route('/books/<int:id>')
def finByid(id):
    # saving found items into an object
    foundBooks = list(filter (lambda t : t["id"] == id, books))
    # if no items found, return the empty list
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    # else return the found item
    return jsonify(foundBooks[0])


# Create a book
# curl -X "POST" -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId

    # Check if the data being sent is in json format
    if not request.json:
        # if not abort
        abort(400)

    book = {
        "id" : nextId,
        "Title" : request.json["Title"], 
        "Author" : request.json["Author"],
        "Price" : request.json["Price"]
    }

    books.append(book)
    nextId += 1

    return jsonify(book)

# Update a value
# curl -X "PUT" -d "{\"Title\":\"New Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter (lambda t : t["id"] == id, books))
    # if no items found, return the empty list
    if len(foundBooks) == 0:
        return jsonify({}) , 404
    
    # the found book
    currentBook = foundBooks[0]

    # Updating all the attributes included in the PUT request
    if "Title" in request.json:
        currentBook["Title"] = request.json["Title"]

    if "Author" in request.json:
        currentBook["Author"] = request.json["Author"]
    
    if "Price" in request.json:
        currentBook["Price"] = request.json["Price"]

    # Return the updated book to the client and the database
    return jsonify(currentBook)

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter (lambda t : t["id"] == id, books))
    # if no items found, return the empty list
    if len(foundBooks) == 0:
        return jsonify({}) , 404
    
    books.remove(foundBooks[0])
    
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)