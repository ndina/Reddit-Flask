from flask import render_template, Blueprint, flash, url_for, redirect
from main.forms import SearchForm
from main.apis import reddit
from prawcore import NotFound

searchapi = Blueprint('search_api', __name__)


@searchapi.route('/search/data_', methods=['POST','GET'])
def search():
    """Search subreddit by data user has entered.
    Checks that the subreddit taken from SearchForm is existing,
    if not give an error text.

    """
    form = SearchForm()
    if search_db(form.string_field.data):
        return redirect(url_for('post.find_reddit', s=form.search.data))
    else:
        flash('Oops .. there is no information about it')


def search_db(s):
    """Bool function which returns true if subreddit exists, and
    false otherwise
    :param isExist: returns 0 or 1, depending on input data

    """
    isExist = True
    try:
        reddit.subreddits.search_by_name(s, exact=True)
    except NotFound:
        isExist = False
    return isExist
