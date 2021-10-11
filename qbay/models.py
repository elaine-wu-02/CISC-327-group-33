from qbay import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Identity
from datetime import date
import re

'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# This is the Transaction class
class Transaction(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    # User's email address.
    # It could be not unique since
    # a same user can have more than one transactions.
    user_email = db.Column(
        db.String(50), nullable=False)
    product_id = db.Column(
        db.String(50), nullable=False)
    price = db.Column(
        db.String(5), nullable=False)
    date = db.Column(
        db.String(20), nullable=False)

    def __repr__(self):
        return '<Transaction %r>' % self.username


# This is the Review class
class Review(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    Id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    user_email = db.Column(
        db.String(50), nullable=False)
    score = db.Column(
        db.String(5), nullable=False)
    # User's review.
    # It could be empty since
    # same user do not leave any text review.
    review = db.Column(
        db.String(200), nullable=True)


# This is the Product class
class Product(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    title = db.Column(
        db.String(50), nullable=False)
    description = db.Column(
        db.String(200), nullable=True)
    price = db.Column(
        db.String(5), nullable=False)
    last_modified_date = db.Column(
        db.String(20), nullable=False)
    owner_email = db.Column(
        db.String(50), nullable=False)


# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]


def Create_product(title, description, last_modified_date, price, owner_email):
    D1 = date(2021, 1, 2)
    D2 = date(2025, 1, 2)
    # Check if the title is in the right format
    if (title.startswith(' ') or
            title.endswith(' ')):
        print("first letter or last letter can't be space, please try again!")
        return None
    pattern = r'[a-zA-Z\s]+'
    if re.match(pattern, title) is None:
        print(" The title of the product has to be alphanumeric-only, and \
            space allowed only if it is not as prefix and suffix. \
                Please try again!")
        return None
    # Check the length of title.
    if len(title) > 80:
        print("the length of title can't be larger than 80, please try again!")
        return None
    # Check the length of description.
    if (len(description) > 200 or
            len(description) < 20):
        print("the length of the description is not correct, \
            please try again!")
        return None
    # Check if the description is longer than title
    if len(description) < len(title):
        print("Description has to be longer than the product's title, \
            please try again!")
        return None
    # Check if the price is in the correct range.
    if not(price in range(10, 10001)):
        print("Price has to be of range [10, 10000]. Please  try again!")
        return None
    # Check if the date is correct.
    if (last_modified_date < D1 or
            last_modified_date > D2):
        print("You can no longer modify this product anymore. \
            The effective is from 2021-01-02 to 2025-01-02. \
                Please try again!")
        return None
        # The email address can't be empty.
    if owner_email is None:
        print("The owner email cannot be empty. Please try again!")
        return None
    Owner_existed = User.query.filter_by(email=owner_email).all()
    if (len(Owner_existed) < 0 or
            (owner_email is None)):
        print("The owner of the corresponding product \
            not exists in the database. Please try again!")
        return None
    # different product can't have same title.
    Title_existed = Product.query.filter_by(title=title).all()
    if len(Title_existed) > 0:
        print("The title of the product has been created already. \
            Please try again!")
        return None

    # create a new product
    product = Product(
        title=title, description=description,
        owner_email=owner_email, price=price,
        last_modified_date=last_modified_date)
    # add it to the current database session
    db.session.add(product)
    # actually save the user object
    db.session.commit()
    return True
