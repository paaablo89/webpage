from flask import Flask
from flask import render_template
app = Flask(__name__)

userlist = ['Agustin', 'Guillermo', 'Victor', 'Nacho', 'Pablo', 'Andres']

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/user")
def users():
    return render_template("users.html", userlist=userlist)

@app.route("/user/<user>")
def user(user):
    return render_template("user.html", user=user)

if __name__ == "__main__":
    app.run()
