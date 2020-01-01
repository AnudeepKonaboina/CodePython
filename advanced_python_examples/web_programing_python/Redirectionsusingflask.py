# Redirecting from one url to to another url using flask
from flask import Flask, redirect, url_for, request, render_template, flash, abort

app = Flask(__name__)


@app.route("/")
def form():
    return render_template('login.html')


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST' and request.form['name'] == 'admin':
        print("Successfully logged in")
        name = request.form['name']
        return redirect(url_for('hello_user', name=name))
    else:
        abort(401)
        name = request.args.get('name')
        return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(debug=True)
