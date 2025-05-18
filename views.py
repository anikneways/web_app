from flask import Blueprint , render_template

views = Blueprint('views_main',__name__)
@views.route('/')
def home():
    return render_template("home.html")
