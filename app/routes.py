from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jason"}
    posts = [
        {"author": {"username": "Jane"}, "body": "Beautiful rainy day here!"},
        {"author": {"username": "Jill"}, "body": "Long day in the office!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

