from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'index deploy!'


@app.route('/page')
def page():
    return 'second page'
