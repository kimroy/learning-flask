from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Renders the index.html which extends the base template
@app.route('/')
def home():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(debug=True)