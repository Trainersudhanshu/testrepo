from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask app!")

@app.route('/greet/<name>')
def greet(name):
    if not name.isalpha():
        abort(400, description="Invalid name")
    return jsonify(message=f"Hello, {name}!")

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        abort(400, description="Missing required parameters")
    
    try:
        a = int(data['a'])
        b = int(data['b'])
    except ValueError:
        abort(400, description="Parameters must be integers")
    
    return jsonify(result=a + b)

@app.errorhandler(400)
def bad_request(error):
    return jsonify(error=str(error)), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True, port=80)
