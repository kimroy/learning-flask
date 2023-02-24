from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Pass the content variabel to the html template which is referenced there with {{var_name}}
@app.route('/<name>')
def home(name):
    # Render #1: return render_template('index2.html', content=name, content2=2)
    # Render #2: return render_template('index2.html')
    # Render #3:
    return render_template('index2.html', content=['a','b','c','d','f'])


if __name__ == '__main__':
    app.run(debug=True)