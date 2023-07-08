from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return render_template('loan.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('login.html')

@app.route('/register_form', strict_slashes=False, methods=['POST', 'GET'])
def register():

    # Render the registration success template
    return render_template('register.html')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')

@app.route('/loan-eligibility Cal', strict_slashes=False)
def calculator():
    return render_template('features.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
