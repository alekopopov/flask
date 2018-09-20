import flask
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
	return "Работи ли бе"

if __name__ == "__main__":
	app.run(debug=True)
