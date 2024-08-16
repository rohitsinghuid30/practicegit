# This is our main app
from flask import Flask
from app import Name

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the flask coding."

@app.route("/register", methods=["GET", "POST"])
def register():
    return "Register employee here"

def sum(a, b):
    return a+b

def substract(a,b):
    return a-b


myname = Name("Rohit Singh")
print(myname)

if __name__ == "__main__":
    app.run(debug=True)
