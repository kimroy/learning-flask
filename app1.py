from flask import Flask, redirect, url_for

app = Flask(__name__)

# Decorate the function such that whenever we go to that domain this function will run
@app.route('/')
def home():
    return 'Hello this is the main page <h1>Hello</h1>'

# Items which are enclosed in the <> are values which are passed as parameters to the function
@app.route('/<name>')
def user(name):
    return f'Hello {name}'

# Redirects the /admin url to the home() function
@app.route('/admin')
def admin():
    return redirect(url_for('home'))

# Redirects the /admin url to the user() function with a parameter passed
@app.route('/admin1')
def admin1():
    return redirect(url_for('user', name='Admin1!'))

if __name__ == '__main__':
    app.run(debug=True)