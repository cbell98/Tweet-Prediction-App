from pickle import FALSE
from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    # configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Connect our database
    DB.init_app(app)

    @app.route("/")
    def home_page():
        # query for the all users table
        users = User.query.all()
        print(users)
        return render_template('base.html', title='Home', users=users)

    @app.route('/populate')
    # Test the database functionality by inserting fake data into DB
    def populate():

        # remove everything from the DB
        DB.drop_all()
        # recreate the user and tweet tables for use
        DB.create_all()

        # Make two new users
        ryan = User(id=1, username='ryanallred')
        julian = User(id=2, username='julian')

        # Make two tweets
        tweet1 = Tweet(id=1, text="this is ryan's tweet", user=ryan)
        tweet2 = Tweet(id=2, text="this is julian's tweet", user=julian)

        # Insert data when working with SQLite directly
        DB.session.add(ryan)
        DB.session.add(julian)
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        # Commit the DB changes
        DB.session.commit()

        return render_template('base.html', title='Populate')
        # Make two tweets and attach the tweets to those users

    @app.route('/reset')
    def reset():
        # Do some database stuff
        # Drop old DB tables
        # Remake new DB tables
        # remove everything from the DB
        DB.drop_all()
        # recreate the user and tweet tables for use
        DB.create_all()
        return render_template('base.html', title='This is the reset page')

    return app
