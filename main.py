from flask import Flask, request, jsonify # We need request and jsonify to handle POST requests
app = Flask(__name__)

# Decorators are a cool Python feature that allow you to modify or extend the behavior
# of callable objects (functions, methods or classes) without permanently modifying the callable itself.
# Timing, caching, logging, authentication, etc. are all examples of cross-cutting concerns that can be implemented

# Use the decorator app.route to tell Flask what URL should trigger our function.
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({'user_id': user_id}), 200

# As we know, we need to jsonify and un-jsonify data when we send and receive it from the server.
# We use postman to test the API with POST methods (desktop version) or curl (command line)
# Also, obviously we would want to store the data in a database, but for now we will just return the data we receive.
@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)