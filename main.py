# Import Flask package 
from flask import Flask, request

# For Checking, What is name 
print("Name:", __name__)
app = Flask(__name__)


## flask --app (file main) run --> In a Production Server
## flask run


## In that An id is given instead of name like above:
# and in this , we can enter 'int' or 'str' , but we only want 
# to get int so we do one thing that is :
# @app.route('/blog/<postID>')
# @app.route('/blog/<int:postID>')
# def showblog(postID):
#     return f"<h1>Blog Number {postID}</h1>"


# This is Route Path And this slash is Home Page that is 
@app.route("/")
def index():
    return "<h1>Hello World<h1>"

# One More page created by another route 
# And Remember this is a routing
@app.route('/user/')
def show_all_users():
    return "<h1>All User!</h1>"

@app.route('/user/', methods=["GET", "POST", "DELETE", "PUT"])
def manage_users():
    if request.method == "POST":
        return "<h1>Create New User!</h1>"
    elif request.method == "DELETE":
        return "<h1>Delete User!</h1>"
    elif request.method == "PUT":
        return "<h1>Update User!</h1>"
    else:
        return "<h1>Show All Users:</h1>"

@app.route('/user/<int:PostID>')
def showblog(PostID):
    return f"<h1>Blog Number {PostID}</h1>"

# Tutorial:- 33:51 time continue tomorrow: