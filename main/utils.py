"""
Utilities for our views and models.
"""
import string
import random
import os
from datetime import datetime, timedelta
from main.apis import reddit
import praw


def get_current_time():
    return datetime.utcnow()


def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    global diff
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now  # type: timedelta
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return  "a minute ago"
        if second_diff < 3600:
            return str( second_diff / 60 ) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str( second_diff / 3600 ) + " hours ago"

    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff/7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff/30) + " months ago"

    return str(day_diff/365) + " years ago"


def get_comments(submission):
    subreddit = reddit.subreddit('python')
    hot_python = subreddit.hot(limit=3)
    commentss = []
    n = 0
    for submission in hot_python:
        if not submission.stickied:
            print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                               submission.ups,
                                                                               submission.downs,
                                                                            submission.visited))
            comments = submission.comments
            for comment in comments:
                print(20 * '-')
                print(comment.body)
                if len(comment.replies) > 0:
                    for reply in comment.replies:
                        print('REPLY:')
                        print("\t" + reply.body)

    for comment in submission.comments:
        if n >= 8:
            break
        commentss.append(comment)
        n += 1
    return commentss