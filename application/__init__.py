from flask import Flask


from config import Config

# from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.init_app(app)
login_manager.login_view='login'




# db=MongoEngine()
# db.init_app(app)

from application import routes



if __name__=="__main__":
    app.run(debug=True)