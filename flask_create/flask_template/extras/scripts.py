from flask_script import Manager
from src import create_app,db
app = create_app
manager = Manager(app)

# add the command and the required script in function
#command name will be init_db
@manager.command
def init_db():
    db.create_all()
    print("Database Initiated! \nThis doesn't handle migrations!")

if __name__ == "__main__":
    manager.run()
