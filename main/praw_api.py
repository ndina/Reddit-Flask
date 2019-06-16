import requests


base_url = 'https://www.reddit.com'


# data = {'grant_type': 'password', 'username': 'dina2505', 'password': 'Dina1976'}
# auth = requests.auth.HTTPBasicAuth('3zs13CrICvZJsA', 'VtgGXKe80yTxrmdtXnbbbiKR2c8')
# r = requests.post(base_url + 'api/v1/access_token',
#                   data=data,
#                   headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'},
# 		          auth=auth)
# d = r.json()

def collection_request():
    r = requests.get(base_url+'/r/'+'Collections/'+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d


def subred(subreddit):
    r = requests.get(base_url+'/r/'+subreddit+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d


def user_requests(username):
    r = requests.get(base_url+'/user/'+username+'/about'+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d


def user_info(username):
    r = requests.get(base_url+'/user/'+username+'/about'+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d


def user_page(username):
    r = requests.get(base_url+'/user/'+username+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d


def thread(subreddit):
    r = requests.get(base_url+'/r/'+subreddit+'.json',
                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36'
                              '(KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'})
    d = r.json()
    return d

