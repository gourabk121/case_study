from flask import render_template, url_for, flash, redirect,flash
from application import app,db,login_manager
from datetime import datetime
from application.forms import Userfrom
from flask_login import UserMixin,logout_user,current_user,login_required,login_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Index')


#  database construction for user   

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    time= db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    designation= db.Column(db.String(20),nullable=False)


    def __repr__(self):
        return f"User('{self.id}','{self.password}','{self.time}','{self.designation}')"


# operational page

@app.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    return render_template('new.html', title='new')




# login part

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return 'you are alraedy logged in'
    form = Userfrom()
    if form.validate_on_submit():
        user=User.query.filter_by(id=form.id.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            flash('Login Sucessfull as','Success')
            return redirect(url_for('new'))
        else:
            flash('unsucessfull please give correct information','danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)



# logout part

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


