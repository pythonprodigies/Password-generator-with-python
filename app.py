import random
import string
import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pdnejoh@18",
    database="passwords"
)
mycursor=database.cursor()

characters=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
def create_password(length):
    password=""
    password=password+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for i in range(length-3):
        password=password+random.choice(characters)
    random.shuffle(list(password))
    password="".join(password)
    return password


length=int(input("Enter the no of characters in password"))
password=create_password(length)
if input("Do you want to save it to the database?(y/n)")=='y':
    need=input("Enter the need of the password")
    link=input("Enter the URL for which you are using this password")
    username=input("Please enter the username")
    data=(need,username,password,link)
    mycursor.execute("insert into passwords(need,username,password,link) values(%s,%s,%s,%s)",data)
    database.commit()
    mycursor.close()
    database.close()
    print(f"The password is added to the database")
    print("The password is",password)
else:
    print(password)
