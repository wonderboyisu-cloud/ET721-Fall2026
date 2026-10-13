"""
Isaam Shah
Oct 13, 2026
Lab 10: intro to Flask
"""

from flask import Flask, render_template, redirect, url_for

"""
Create an object named "app" from the Flask module.
__name__ set to __main__ if the script is running directly from main file
"""

app = Flask(__name__)

# set the routing to main page (loading page)
# "route" decorator is used to access the root URL

@app.route("/")
def index():
    name = "Isaam Shah"
    fruits = ["apple", "pineapple", "oranges"]
    return render_template("index.html", username = name, listfruits = fruits)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/quotes")
def quotes():
    # redirect to index route
    return redirect(url_for("index"))

# set the "app" to run if you execute the file directly (not when it is imported)
if __name__ == "__main__":
    app.run(debug=True)














