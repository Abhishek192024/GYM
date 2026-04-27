from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to ACEest Fitness & Gym"

@app.route('/members')
def members():
    data = [
        {"id": 1, "name": "Anita", "plan": "Gold"},
        {"id": 2, "name": "Abhishek", "plan": "Silver"}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)