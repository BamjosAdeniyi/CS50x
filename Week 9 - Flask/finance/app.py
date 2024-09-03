import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""
    # Get user's stocks and shares
    user_id = session.get("user_id")
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", user_id)

    # Get user's cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']

    # Initialize variables for total values
    total_value = cash
    grand_total = cash

    # To iterate over the stocks and add price and total value
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["value"] = quote["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        if not symbol:
            return apology("You must provide symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("You must provide a positive integer number of shares")

        shares = int(shares)  # Ensure shares is an integer
        quote = lookup(symbol)
        if quote is None:
            return apology("Symbol not found")

        price = quote["price"]
        total_cost = shares * price  # Ensure total_cost is correctly calculated

        user_id = session.get("user_id")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']

        if cash < total_cost:
            return apology("There is not enough cash")

        # Update the users table
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Add the purchase to the transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)", user_id, symbol, shares, price)

        flash(f"Bought {shares} shares of {symbol} for {usd(total_cost)}!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # Show registration form
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check for error
        registered_users = db.execute(
            "SELECT username FROM users WHERE username=?", username
        )

        if not username:
            return apology("Must provide username", 400)

        elif registered_users:
            return apology("Username is not available", 400)

        elif password == "":
            return apology("Enter Password!", 400)

        elif validate_password(password) == False:
            return apology("Invalid Password", 400)

        elif confirmation == "":
            return apology("Must provide password confirmmation", 400)

        elif password != confirmation:
            return apology("Passwords do not match", 400)

        # Hash the password
        password_hash = generate_password_hash(password)

        # Add user to the DB
        query = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password_hash)

        if query:
            # Log in the user
            user_data = db.execute("SELECT id FROM users WHERE username = ?", username)
            if user_data:
                user_id = user_data[0]["id"]
                session["user_id"] = user_id

                # Redirect user to the index page
                return redirect("/")

        # Return an apology if registration fails
        return apology("Registration failed", 400)

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session.get("user_id")
    # Get user's stock
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", user_id)

    # When user submits the form
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        
        if not symbol:
            return apology("You must provide a symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("You must provide a positive integer number of shares")
        else:
            shares = int(shares)

        # Ensure the stock exists in the user's portfolio
        found_stock = None
        for stock in stocks:
            if stock["symbol"] == symbol:
                found_stock = stock
                break
        
        if not found_stock:
            return apology("Symbol not found")

        if found_stock["total_shares"] < shares:
            return apology("Not enough shares")

        # Get Quote
        quote = lookup(symbol)
        if quote is None:
            return apology("Symbol not found")

        price = quote["price"]
        total_sale = shares * price

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale, user_id)

        # Record the sale in the transactions table (note negative shares for selling)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)", user_id, symbol, -shares, price)

        flash(f"Sold {shares} shares of {symbol} for {usd(total_sale)}!")
        return redirect("/")

    # If the user visits the page
    else:
        return render_template("sell.html", stocks=stocks)

