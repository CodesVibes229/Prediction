from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration de la connexion à MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'LicenceMonetiqueWeb@229'
app.config['MYSQL_DB'] = 'analyse'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/go_to_app2')
def go_to_app2():
    return redirect("http://127.0.0.1:5001")

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('user_login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/account')
def user_account():
    if 'username' not in session:
        return redirect(url_for('user_login'))
    return render_template('user_account.html', username=session['username'])

@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Identifiants incorrects. Veuillez réessayer.')
    return render_template('user_login.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect((url_for('dashboard')))
        else:
            flash('Identifiants incorrects. Veuillez réessayer.')
    return render_template('admin_login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='scrypt')

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        account = cursor.fetchone()

        if account:
            flash('Utilisateur déjà existant ! ', 'danger')
            return redirect(url_for('create_account'))
        else:
            cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, hashed_password))
            mysql.connection.commit()
            cursor.close()
            flash('Vous avez été enregistré avec succès !', 'success')
            return redirect(url_for('user_login'))
    return render_template('create_account.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('user_login'))

if __name__ == '__main__':
    app.run(debug=True,port=5000)
