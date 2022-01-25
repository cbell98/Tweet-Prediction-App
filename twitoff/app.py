from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():
    '''Function to create app'''

    app = Flask(__name__)

    # configuration variable to our app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect our database to the app object
    DB.init_app(app)

    @app.route("/")
    def home_page():
        '''Query for all users in the database'''
        users = User.query.all()
        # print(users)
        return render_template('base.html', title='Home', users=users)

    @app.route('/populate')
    # Test the database functionality by inserting fake data into DB
    def populate():
        '''Remove all data and then insert created data, add, commit'''
        # Reset and remove everything from the DB
        DB.drop_all()
        # Recreate the user and tweet tables for use (inserted into)
        DB.create_all()

        # Make two new users
        ryan = User(id=1, username='ryanallred')
        julian = User(id=2, username='julian')

        # Make six tweets
        tweet1 = Tweet(id=1, text="this is ryan's tweet", user=ryan)
        tweet2 = Tweet(id=2, text="this is julian's tweet", user=julian)
        tweet3 = Tweet(id=3, text="Ryan signing on for the day. GM", user=ryan)
        tweet4 = Tweet(
            id=4, text="Julian signing on for the day.", user=julian)
        tweet5 = Tweet(
            id=5, text="Ryan signing off for the day. GN", user=ryan)
        tweet6 = Tweet(
            id=6, text="Julian signing off for the day.", user=julian)

        # Insert data into DB when working with SQLite directly
        DB.session.add(ryan)
        DB.session.add(julian)
        DB.session.add(tweet1)
        DB.session.add(tweet2)
        DB.session.add(tweet3)
        DB.session.add(tweet4)
        DB.session.add(tweet5)
        DB.session.add(tweet6)

        # Commit the DB changes
        DB.session.commit()

        return render_template('base.html', title='Populate')

    @app.route('/reset')
    def reset():
        '''Drop old DB tables, remake new DB tables'''
        # remove everything from the DB
        DB.drop_all()
        # recreate the user and tweet tables for use (inserted into)
        DB.create_all()

        return render_template('base.html', title='Reset Database')

    return app
