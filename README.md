flask create readme

## Flask-Create

#### Author: Deekshith Anand

### A python package to create production grade flask boiler plate setup.

## Usage:

Create venv inside the project folder.

    	pip install flask-create

Once it is installed, in your root project directory hit this:

    	flask-create

That's it you are all set and good to go!

### Important!

You need to create a .env file with key value pairs containing all the required credentials.

### Default Factory setup

This approach embraces blueprints. It is implemented in the template. All your code lies inside the src, which can be treated like a package.
The other related files like config files, scripts files, etc . . are included outsied src(which will be you project repo)

#### To init db /invoke SQLAlchemy creatall():

Define your models in models.py . A default script is provided in scripts.py.You can have your own scripts defined here along with their equivalent commands(Look into flask-script extension for more).
To int db run this from outside src(i.e., root project folder):

    	python scripts.py init-db

#### To run flask app run this from root folder where flask-create was called:

    	python wsgi.py

##### Note : - The default config is provided for dev. Production config can be modified by user in config.py
