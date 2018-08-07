from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello guardian!!, Im your Ghost!'

@app.route("/user/<user>")
def user(user):
    return "Perfil del guardian %s" % user

if __name__ == "__main__":
    app.run()
