from flask import Blueprint, request

bp = Blueprint("web", __name__)

# This is Route Path And this slash is Home Page that is 
@bp.route("/")
def index():
    return "<h1>Hello World<h1>"

