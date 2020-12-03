from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

host = 'http://127.0.0.1.5000/'


@app.route('/', methods=['POST', 'GET'])
def blockchain_login():
    error = None
    session['current_user'] = ""
    if request.method == 'POST':
        if login_credentials(request.form['username'], request.form['password']):
            session['current_user'] = request.form['username']
            return redirect(url_for('intial_page_ERP'))
        else:
            error = 'invalid username or password'
    return render_template('index.html', error=error)


@app.route('/blockchainERP', methods=['POST', 'GET'])
def intial_page_ERP():
    error = None
    username = get_login_info(session.get('current_user', None))
    return render_template('Blockchain_home.html', error=error, username=username)


def login_credentials(username, password):
    connection = sqlite3.connect('database.db')
    cursor = connection.execute('SELECT * FROM login WHERE username = ? AND password = ?;', (username, password))
    return cursor.fetchone()


def get_login_info(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.execute("SELECT * FROM login WHERE username = ?;", (username,))
    return cursor.fetchall()[0][0]


if __name__ == '__main__':
    app.run(debug=True)
