from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "mjb"}
    posts = [
        {"author": {"username": "Mario"}, "body": "Beautiful, rainy, day at home."},
        {"author": {"username": "Jason"}, "body": "Goodness, what a downpour"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Hello {form.username.data}, you have successfully logged in. Remember me set to {form.remember_me.data}"
        )
        return redirect("/index")
    return render_template("login.html", title="Login Page", form=form)
