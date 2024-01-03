# Import Flask package 
from app.blueprints import web, user
from flask import Flask, request, render_template


app = Flask(__name__)
app.register_blueprint(web.bp)
app.register_blueprint(user.bp)

## flask --app (file main) run --> In a Production Server
## flask run
