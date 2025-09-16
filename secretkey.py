from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return "Flask app with secret key works!"

if __name__ == "__main__":
    app.run(debug=True)
