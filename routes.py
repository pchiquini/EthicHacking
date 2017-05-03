from flask import Flask, render_template, request, session, redirect, url_for
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    else:
    	flash('wrong password!')
    return home()

@app.route("/home")
def home():
  return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)