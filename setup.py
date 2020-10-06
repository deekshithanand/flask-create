import re

from setuptools import setup, find_packages

with open("flask_create/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# pre - required pckages

PACKAGES = ['click==7.1.2',
            'Flask==1.1.2',
            'Flask-Login==0.5.0',
            'Flask-SQLAlchemy==2.4.3',
            'Flask-WTF==0.14.3',
            'itsdangerous==1.1.0',
            'Jinja2==2.11.2',
            'MarkupSafe==1.1.1',
            'python-dotenv==0.13.0',
            'SQLAlchemy==1.3.17',
            'Werkzeug==1.0.1',
            'WTForms==2.3.1']


with open("README.md", "r") as fh:
    README = fh.read()


setup(
    name="flask-create",
    author="Deekshith Anand",
    author_email="deekshith27anand@gmail.com",
    install_requires=PACKAGES,
    description="A tool to create flask boilerplate code",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/deekshithanand/flask-create.git",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version=version,
    entry_points = {
        'console_scripts': ['flask-create=flask_create.create:create'],
    },
    include_package_data=True,
)
