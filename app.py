import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///general.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show main page"""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passoword and password confirmation was the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords not identical", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Check that username doesn't already exist
        if len(rows) != 0:
            return apology("invalid username. This username is already used for an account", 400)

        # Add account to login database and update login database
        update = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")))
        rows = update

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/data", methods=["GET","POST"])
def data():

    if request.method == "POST":
        return redirect("/data")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # get all data from general.db and input into html template as a var
        all_data = db.execute("SELECT * FROM total ORDER BY event")
        return render_template("data.html", data = all_data)

@app.route("/quicksearch", methods=["GET","POST"])
def quicksearch():

    if request.method == "GET":

        all_data = db.execute("SELECT * FROM total ORDER BY event")

        # get all data from general.db and input into html template as a var
        return render_template("quicksearch_result.html", data = all_data)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        menu = request.form.get("menu")

         # get the user data using the request.form.get (reference birthdays)

        if menu == "event_open_men":
            data = db.execute("SELECT * FROM total WHERE event = 'Open Men' ORDER BY time;")

        if menu == "event_open_women":
            data = db.execute("SELECT * FROM total WHERE event = 'Open Women' ORDER BY time;")

        if menu == "event_u23_men":
            data = db.execute("SELECT * FROM total WHERE event = 'U23 Men' ORDER BY time;")

        if menu == "event_u23_women":
            data = db.execute("SELECT * FROM total WHERE event = 'U23 Women' ORDER BY time;")

        if menu == "event_u19_men":
            data = db.execute("SELECT * FROM total WHERE event = 'U19 Men' ORDER BY time;")

        if menu == "event_u19_women":
            data = db.execute("SELECT * FROM total WHERE event = 'U19 Women' ORDER BY time;")

        if menu == "distance_2k":
            data = db.execute("SELECT * FROM total WHERE distance = '2K';")

        if menu == "distance_6k":
            data = db.execute("SELECT * FROM total WHERE distance = '6K';")

        if menu == "classification":
            data = db.execute("SELECT * FROM total ORDER BY classification DESC;")

        if menu == "time":
            data = db.execute("SELECT * FROM total ORDER BY time;")

        # get data from general.db and input into html template as a var
        return render_template("quicksearch_result.html", data = data)
