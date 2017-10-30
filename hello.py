from flask import Flask, render_template, url_for, request, redirect, flash, session

import os

app = Flask(__name__)

import logging
from logging.handlers import RotatingFileHandler

# @app.route('/')
# def index():
# 	return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash('Successfully logged in!')
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username or password'
            app.logger.warning('Incorrect username or password for user "%s"', request.form.get('username'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))


# helper function to decide "correct" login
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


# @app.route('/<string:page_name>/')
# def static_page(page_name):
#     return render_template('%s.html' % page_name)


app.secret_key = '\xa6R?W0\xed\x16\x8d\xc7\n1\xb4:]@\x01q\xbc\x94\x0b\xf88x\xb0'
handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

if __name__ == '__main__':
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run(host='0.0.0.0', port=5001)
