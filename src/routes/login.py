from flask import Blueprint, session, request, redirect, url_for, render_template
from src.db.db_pymysql import BaseData

logins = Blueprint('login', __name__)

db = BaseData(host='', user='root', password='', db='')

@logins.route('/')
def admin():
    return redirect(url_for('login.login'))

@logins.route('/acceso-login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'txtUsername' in request.form and 'txtPassword' in request.form:
        _username = request.form['txtUsername']
        _password = request.form['txtPassword']
 
        cur = db.connection.cursor()  # Obtener un cursor válido desde la conexión

        try:
            cur.execute('SELECT * FROM usuarios WHERE username = %s AND password = %s', (_username, _password,))
            account = cur.fetchone()
        except Exception as e:
            print(f"Error al ejecutar la consulta SQL: {str(e)}")
            account = None

        cur.close()

        if account:
            session['logueado'] = True
            session['id'] = account[0]
            session['deslogueado'] = False

            return redirect(url_for('login.admin'))
    
    return render_template('login.html')
