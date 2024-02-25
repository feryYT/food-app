'''from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from Flask_food_goiteens import User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.db'
db = SQLAlchemy(app)

def test_html():
    name = "Test_Name"
    surname = "test_surname"
    password = "test_password"
    email = "test_email"
        
    users = User(name=name, surname=surname, email=email, password=password)
    db.session.add(users)
    db.session.commit()
    print('start db')
    
    
    
if __name__ == '__main__':
    test_html()
    
''' 
