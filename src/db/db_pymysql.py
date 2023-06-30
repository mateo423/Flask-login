import pymysql

class BaseData:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = pymysql.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            db=self.db
        )
    
    def cursor(self):
        self.connection.cursor()