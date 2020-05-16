from flask import Flask, redirect, url_for, render_template, request, flash
from dotenv import load_dotenv
from pymongo import MongoClient
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/home")
def redirect_home():
	return redirect(url_for("home"))


@app.route("/inventory")
def inventory():
	return render_template("inventory.html")

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	print("SERVER START!")
	app.run(debug=False, host="localhost", port=80)
	print("SERVER CLOSED")