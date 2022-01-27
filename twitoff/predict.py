from .models import User
from sklearn.linear_model import LogisticRegression
import numpy as np
from .twitter import vectorize_tweet


def predict_user(user0_username, user1_username, hypo_tweet_text):
    '''
    Determine and returns which user is more likely to say a given tweet
    Example run: predict_user("elonmusk", "jackblack", "Tesla cars go vroom")
    Returns a 0 (user0_name: "elonmusk") or a 1 (user1_name: "jackblack")
    '''

    # Query for the two users so we can get their embeddings
    user0 = User.query.filter(User.username == user0_username).one()
    user1 = User.query.filter(User.username == user1_username).one()

    # Get the word embeddings
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # Combinging the two users word embeddings into one big 2D numpy array
    # This is essentially our X matric for training our logistic regression
    vects = np.vstack([user0_vects, user1_vects])

    # Create a np array to represent the y vector (indicate which user)
    # was the autor of any given word embedding

    labels = np.concatenate([np.zeros(len(user0.tweets)),
                             np.ones(len(user1.tweets))])

    # import and train logistic reg
    log_reg = LogisticRegression()

    # train
    log_reg.fit(vects, labels)

    # Get the word embeddings for our hypo_tweet_text
    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text)

    # Generate a prediction
    prediction = log_reg.predict([hypo_tweet_vect])

    return prediction[0]
