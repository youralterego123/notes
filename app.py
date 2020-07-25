from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
import re


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/signup'
db = SQLAlchemy(app)

class Sign(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=True, nullable=False)



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if(request.method=='POST'):
        y=0
        email=request.form.get('uname')
        password=request.form.get('psw')
        em=Sign.query.all()
        for x in em:
            if(email==x.email and password==x.password):
                y=1
                return render_template("notes.html",email=email)
        if(y==0):
            return render_template("invalid.html")   

        
    
    return render_template("login.html")
      



@app.route('/signup', methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        email=request.form.get('email')
        password=request.form.get('psw')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
       
        if(re.search(regex,email)):
            entry= Sign(email=email,password=password)
            db.session.add(entry)
            db.session.commit()
            return render_template("signupsucess.html")
        else:
            return render_template("invalid.html")

    return render_template("signup.html")





if __name__=="__main__":
 app.run(debug=True)

