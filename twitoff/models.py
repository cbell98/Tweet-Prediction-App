from flask_sqlalchemy import SQLAlchemy


# Create a DB Object

DB = SQLAlchemy()


# Create a table with a specific schema
# We will do that by creating a python class.

class User(DB.Model):
    # Two columns inside of our user table
    # ID Column Schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # Username Column Schema
    username = DB.Column(DB.String, nullable=False)
    # Tweets list is created by the .relationship and backref in the Tweets class
    # tweets = []


class Tweet(DB.Model):

    # ID Column Schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # Text Column Schema
    text = DB.Column(DB.Unicode(300), nullable=False)
    # User Column Schema (Secondary/Foreign Key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    # Set up a relationship between the tweets and the users
    # Will automatically create the one-to-many relationship, but also
    # add a new attribute onto the "User" class called "tweets" which
    # will be a list of all of the user tweets
    user = DB.relationship("User", backref=DB.backref('tweets'), lazy=True)
