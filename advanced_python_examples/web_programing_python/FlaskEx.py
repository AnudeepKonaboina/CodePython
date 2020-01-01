# Example of flask
# Importing flask module in the project is mandatory. An object of Flask class is WSGI application.
# Flask constructor takes the name of current module (__name__) as argument.
# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function
# the run() method of Flask class runs the application on the local development

from flask import Flask as fs

app = fs(__name__)


@app.route("/hello")
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
