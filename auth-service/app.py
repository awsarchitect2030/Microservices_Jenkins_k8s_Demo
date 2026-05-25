from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    return jsonify({
        "message": "Login Microservice Running"
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)