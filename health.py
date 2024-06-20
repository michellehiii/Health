from flask import Flask, render_template

# Create a Flask Instance 
app=Flask(__name__)

# Create a Route Decorator 
@app.route('/')

# def index():
#     return "<h1> Health </h1>"

def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Invalid URL
@app.errorhandler(404)
def pag_not_found(e):
    return render_template("404.html"), 404

# Interal Server Error
@app.errorhandler(500)
def pag_not_found(e):
    return render_template("500.html"), 500