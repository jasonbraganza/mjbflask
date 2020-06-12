from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "mjb"}
    posts = [
        {"author": {"username": "Mario"}, "body": "Beautiful, rainy, day at home."},
        {"author": {"username": "Jason"}, "body": "Goodness, what a downpour"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
