from flask import Flask , render_template , redirect , request  
from flask_sqlalchemy import SQLAlchemy
from Flask_food_goiteens import User


app = Flask(__name__)


@app.route('/show_data')
def show_data():
    data = User.query.all() 
    return render_template("show_data.html" , data=data)

if __name__ == '__main__':
    app.run(debug=True)
