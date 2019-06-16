from main.praw_api import user_page, user_requests
from main.utils import pretty_date
from flask import Blueprint, render_template

userapi = Blueprint('user_api', __name__)


@userapi.route('/user/<string:username>')
def user_api(username):
    """For user's profile information.
    Sending request to user_requests function
    Returns the information from '/r/u/username reddit api'

    """
    user_r = user_requests(username)
    data = user_page(username)
    return render_template('user.html', user=user_r['data'], datas=data['data']['children'])


# TODO: finish to bind with reddit api
@userapi.route('/login')
def login():
    return render_template('auth.html')


# TODO: finish to bind with reddit api
@userapi.route('/singup')
def sign():
    return render_template('signup.html')


