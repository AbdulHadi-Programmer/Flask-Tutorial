from flask import Blueprint, request, render_template, redirect, url_for
bp = Blueprint("app", __name__)


@bp.route('/user/', methods=["GET", "POST"])
def manage_users():
    if request.method == "POST":
        # return request.form
        # return "<h1>Create New User!</h1>"
        return redirect(url_for("index.html"))
    else:
        return render_template("user/index.html")



@bp.route("/user/create")
def create():
    return url_for("user.create")
    # return render_template("user/create.html")


    
@bp.route('/user/<int:id>', methods=["DELETE", "PUT"])
def user_id(id):
    if request.method == "DELETE":
        return "<h1>Delete User!</h1>"
    elif request.method == "PUT":
        return "<h1>Update User!</h1>"
    
@bp.route('/user/<int:id>')
def about(id):
    # return f'<h1>Welcome {id}</h1>'
    return render_template("user/show.html", id=id)