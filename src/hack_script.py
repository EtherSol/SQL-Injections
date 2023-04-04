import mysql.connector 
from database import users
from account_class import UserDatabase


username = input("Username: ")
password = input("Password: ")

user = (username, password)
account1 = "Account info with\n" + str(user)

print(user[0])

UserDatabase("127.0.0.1", username,password,users)



