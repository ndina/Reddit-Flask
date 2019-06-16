from main.praw_api import subred
from flask import Blueprint, render_template
from main.apis import reddit
from main.utils import get_comments

postapi = Blueprint('post_api', __name__)


@postapi.route('/')
def main_page():
    """Get a posts of main reddit front page where subreddit
       with key 'all'.

    """
    posts = subred('all')
    return render_template('home.html', posts=posts['data']['children'])


@postapi.route('/posts/<string:id>')
def comments(id):
    """ Get a post and its comments by post's id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    return the post with author and comment information

    """
    post = reddit.submission(id=id)
    comments = get_comments(post)
    return render_template('post.html', post=post, comments=comments)


@postapi.route('/r/<string:s>')
def find_reddit(s):
    """Get a posts of certain subreddit. """
    posts = subred(s)
    return render_template('subreddit.html', posts=posts['data']['children'])






