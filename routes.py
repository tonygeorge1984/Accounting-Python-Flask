from flask import Flask 
from werkzeug.utils import html

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to Accounting Page</h1>"


@app.route("/about")
def home():
    return "<h1>Welcome to About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
