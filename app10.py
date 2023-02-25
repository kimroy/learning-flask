from flask import Flask, render_template
from app10_2 import app10_2

app = Flask(__name__)
app.register_blueprint(app10_2, url_prefix='/admin')

@app.route('/')
def test():
    return '<h1>main file</h1>'

if __name__ == '__main__':
    app.run(debug=True)
