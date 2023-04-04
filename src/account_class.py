import mysql.connector 

class UserDatabase: 
    def __init__(self,host,username,password,database):
        self.host = host 
        self.username = username 
        self.password = password
        self.database = database 
        self.connection = None 
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            username = self.username,
            password = self.password,
            database = self.database
        )
    
    def add_user(self,user,password):
        self.connect()
        cursor = self.connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (user, password)
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()
        self.disconnect()
    
    def get_all_users(self):
        self.connect()
        cursor = self.connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        self.disconnect()
        return result
