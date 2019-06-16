from main.praw_api import collection_request
from flask import render_template, Blueprint

collectionapi = Blueprint('collection', __name__)


@collectionapi.route('/collections/')
def col():
    """ Sending request to collections_request function"""
    collections = collection_request()
    return render_template('collection.html', posts=collections['data']['children'])