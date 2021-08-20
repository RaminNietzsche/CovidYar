from flask import Blueprint, render_template

mod = Blueprint('main', __name__, url_prefix='/')

@mod.route('/')
def index():
	return render_template("index.html")