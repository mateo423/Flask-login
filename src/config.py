from flask import Flask
from src.db.db_pymysql import BaseData
from src.routes.login import logins





app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = '19af8d2176878bc9230cf163c129437e0be85bdc7c66474547d72dbfa4b35814'
#Connection BaseDatos



db = BaseData(host='', user='root', password='', db='')


    #BluePrints

app.register_blueprint(logins)

