from flask import Flask, render_template, request, session, redirect, url_for, make_response
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)
blog_posts = []

cookiesDict = {}

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/incorrect")
def incorrect():
  return render_template("incorrect.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        session['username'] = request.form['username']
        resp = make_response(redirect('/home'))
        resp.set_cookie('sessionID', "cookie")
        cookiesDict["cookie"] = "admin"
        return resp
    else:
    	return redirect(url_for('incorrect'))
    return home()

@app.route("/home", methods = ["POST", "GET"])
def home():
	cookie = request.cookies.get("sessionID")
	
	if cookie not in cookiesDict:
		return "Error"
	
	user = cookiesDict[cookie]

	if request.method == "POST":
		text = request.form['text']
		blog_posts.append(text)
		print(blog_posts)
		return render_template('home.html', blog_posts=blog_posts)
	else:
		return render_template("home.html")

if __name__ == "__main__":
  app.run('0.0.0.0', 5000)










