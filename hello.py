from flask import Flask, render_template, url_for, request, redirect, flash
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash('Successfully logged in!')
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = 'Incorrect username or password'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/login/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)


# helper function to decide "correct" login
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


# @app.route('/<string:page_name>/')
# def static_page(page_name):
#     return render_template('%s.html' % page_name)


app.secret_key = 'SuperSecretKey'
if __name__ == '__main__':
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run(host='0.0.0.0', port=5001)
