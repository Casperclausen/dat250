import os
import sqlite3
from flask import *
from werkzeug.security import *
from usersdb import insert_user, get_users
 
app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'


def get_db():
    if not hasattr(g, "_database"):
        print("create connection")
        g._database = sqlite3.connect("database.db")
    return g._database

        
def valid_login(username, password):
    """Checks if username-password combination is valid."""

    db = get_db()
    user = get_users(db,username)
    if not user:
        return False
    generate_password_hash("rawPassword")
    if user:
        return check_password_hash(user["password"], password)
    return False


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data['username']
        password = data['password']
        if valid_login(username, password):
            db = get_db()
            user = get_users(db, username)
            if user:
                session["username"] = user["username"]
                session["role"] = user["role"]
            return '', 200
        else:
            return jsonify({"error": "Invalid username or password!"}), 400
    return render_template("login.html")

@app.route("/secrets")
def showsecrets():
    username = session.get("username")
    role = session.get("role")
    if not username:
        flash("You need to log in")
        return redirect(url_for("login"))
    if role !="admin":
        abort(403)
    return "Hello admin : {}".format(username)


@app.route('/signup', methods=['GET', 'POST'])
def register():
    name = ''
    pw = ''
    if request.method == 'POST':
        name = request.form.get("username")
        pw = request.form.get("password")
        if not pw:
            flash("Please enter a password")
            return redirect(url_for("register"))
        if len(pw) < 5:
            flash("Please enter a password with more than 4 characters.")
            return redirect(url_for("register"))
        db = get_db()
        ok = insert_user(db, name, generate_password_hash(pw))
        if not ok:
            flash("Username is not available, try something else")
        else:
            flash("Registration was successful. Please log in.")
            return redirect(url_for("login"))
    return render_template('register.html')
 

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("store"))


@app.route("/")
def store():
     return render_template("store.html", username=session.get("username", None))
 
@app.route("/about")
def about():
     return render_template("about.html", username=session.get("username", None))
 

@app.route("/account")
def account():
     return render_template("account.html",username=session.get("username", None))
 
@app.route("/contact")
def contact():
     return render_template("contact.html",username=session.get("username", None))

@app.route("/deal")
def deal():
     return render_template("deal.html",username=session.get("username", None))

@app.route("/best-seller")
def best_seller():
     return render_template("best-seller.html", username=session.get("username", None))
 
@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        print("close connection")
        db.close()

if __name__ == "__main__":
    app.run(debug=True)