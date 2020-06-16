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
            "Hello {}, you have successfully logged in. Remember me set to {}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
