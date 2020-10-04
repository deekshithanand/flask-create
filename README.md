[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

# Flask-Create

## ABOUT

Flask-create is a cli tool, something similar to create-react-app in the React Universe! The main purpose of this tool is to provide with a boiler plate code , with production grade quality in mind! Along with default setup, the tool also aims to provides flexibility to optin for user-defined setup. This user defined setup needs to be copied from an existing project,which can be later used insted of the regular setup!

### What powers flask-create?

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Flask-create is made possible using python and other related packaging tools!

# Usage:

- Create venv inside the project folder.

  	pip install flask-create

- Once it is installed, in your root project directory hit this:

  	flask-create

That's it you are all set and good to go!

### Important!

- You need to create a .env file with key value pairs containing all the required credentials.

## Default Factory setup

- This approach embraces blueprints. It is implemented in the template. All your code lies inside the src, which can be treated like a package.
- The other related files like config files, scripts files, etc . . are included outsied src(which will be you project repo)

### To init db /invoke SQLAlchemy creatall():

Define your models in models.py . A default script is provided in scripts.py.You can have your own scripts defined here along with their equivalent commands(Look into flask-script extension for more).
To int db run this from outside src(i.e., root project folder):

    	python scripts.py init-db

### To run flask app run this from root folder where flask-create was called:

    	python wsgi.py

##### Note : - The default config is provided for dev. Production config can be modified by user in config.py


# Build Instructions

Build a python package:

```
python3 -m venv venv
source venv/bin/activate

pip install wheel

python setup.py bdist_wheel
# Produces a .whl file in dist/
```

# Note for Contributing

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features

## Making a PR

- Fork the repo and clone it on your machine.
- Add a upstream link to main branch in your cloned repo

  ```
   git remote add https://github.com/sauravhiremath/fifa-stats-crawler.git

  ```

- Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

  ```
  git pull upstream master
  ```

- Create your feature branch
  ```
  git checkout -b <feature-name>
  ```
- Commit all the changes
  ```
  git commit -am "Meaningful commit message"
  ```
- Push the changes for review
  ```
  git push origin <branch-name>
  ```
- Create a PR from our repo on Github.

### Additional Notes

- Code should be properly commented to ensure it's readability.
- If you've added code that should be tested, add tests as comments.
- In python use docstrings to provide tests.
- Make sure your code properly formatted.
- Issue that pull request!

## Issue suggestions/Bug reporting

When you are creating an issue, make sure it's not already present. Furthermore, provide a proper description of the changes. If you are suggesting any code improvements, provide through details about the improvements.

**Great Issue suggestions** tend to have:

- A quick summary of the changes.
- In case of any bug provide steps to reproduce
  - Be specific!
  - Give sample code if you can.
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

### Additional References:

More step by step guide with pictures for creating a pull request can be found [here](https://opensource.com/article/19/7/create-pull-request-github)
