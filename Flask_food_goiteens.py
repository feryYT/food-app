from flask import Flask , render_template , redirect , request  
from my_api import search_recipes

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    surname = db.Column(db.Text, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    

    

with app.app_context():
    def test_html():
        name = "Test_Name"
        surname = "test_surname"
        password = "test_password"
        email = "test_email"
        
        my_test = User(name=name, surname=surname, email=email, password=password)
        db.session.add(my_test)
        db.session.commit()
        print('start db')
        
    
    def test_sql():
        users = User.query.all()
        for user in users:
            print(user.name)
            print(user.surname)
            print(user.password)
            print(user.email)
        

@app.route('/login_page')
def log_page():
    return render_template("login.html")

@app.route('/for_admins')
def for_admins():
    posts = User.query.all() 
    return render_template("for_admins.html" , users = posts)

@app.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        surname = request.form["surname"]
        password = request.form["password"]
        email = request.form["email"]
        
        user = User.query.filter_by(name=name, surname=surname, email=email, password=password).first()
        if user:
            return redirect('/')
        else:
            return redirect('/home')
        
@app.route('/reg_page')
def reg_page():
    return render_template("register.html")

@app.route('/reg', methods=["POST"])
def reg():
    if request.method == 'POST':
        name = request.form["name"]
        surname = request.form["surname"]
        password = request.form["password"]
        email = request.form["email"]
        
        users = User(name=name, surname=surname, email=email, password=password)
        db.session.add(users)
        db.session.commit()
        return redirect('/login_page')

@app.route("/home")
def home():
    cabbage='''Название: Cream of red cabbage soup
    ID: 640544
    Рейтинг: Неизвестно
    Время приготовления: 45 мин.

    Название: Curried Cabbage & Kale Gratin
    ID: 641060
    Рейтинг: Неизвестно
    Время приготовления: 45 мин.

    Название: Slow Cooked Corned Beef and Cabbage
    ID: 660266
    Рейтинг: Неизвестно
    Время приготовления: 500 мин.

    Название: Cabbage and Sausage Casserole
    ID: 1697585
    Рейтинг: Неизвестно
    Время приготовления: 165 мин.

    Название: Savoy Cabbage and Celery Root Soup with Leek Confit
    ID: 659513
    Рейтинг: Неизвестно
    Время приготовления: 45 мин.'''
    cucumber = ''''''

    return render_template('home.html')

    
if __name__ == '__main__':
   with app.app_context():
    db.create_all()
    #test_html()
    test_sql()
   app.run(debug=True)

