from flask import Blueprint, render_template

app10_2 = Blueprint('app10_2', __name__, static_folder='static', template_folder='templates')

@app10_2.route('/home')
@app10_2.route('/')
def home():
    return render_template('home9.html')
