import praw
"""
Creating an app
~~~~~~~~~~~~~~~
After submitting the app details, we get a public key and a secret key.
This key pair is required to use the Reddit API.

"""

reddit = praw.Reddit(client_id='3zs13CrICvZJsA',
                     client_secret='VtgGXKe80yTxrmdtXnbbbiKR2c8',
                     username='dina2505',
                     user_agent='redditClone',)