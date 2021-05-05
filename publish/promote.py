import requests
import json

with open('keys.json', 'r') as fIn:
    KEYS = json.load(fIn)

def tweet(tweet):
    import tweepy
    auth = tweepy.OAuthHandler(KEYS['twitter']['api_key'], KEYS['twitter']['api_secret_key'])
    auth.set_access_token(KEYS['twitter']['access_token'], KEYS['twitter']['access_token_secret'])
    api = tweepy.API(auth)
    api.update_status(tweet)
    print('Published on Twitter')

def post_on_reddit(message, link, subs):
    import praw
    reddit = praw.Reddit(client_id=KEYS['reddit']['client_id'],
                        client_secret=KEYS['reddit']['client_secret'],
                        user_agent=KEYS['reddit']['user_agent'],
                        redirect_uri=KEYS['reddit']['redirect_uri'],
                        refresh_token=KEYS['reddit']['refresh_token'])

    for subr in subs:
        subreddit = reddit.subreddit(subr)
        subreddit.submit(title, url=link)

def shorten_url(url):
    header = {
        "Authorization": f"Bearer {KEYS['bitly']['token']}",
        "Content-Type": "application/json"
    }
    params = {"long_url": url}
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
    data = response.json()
    if 'link' in data.keys():
        print('Shortened URL')
        return data['link']
    else:
        print("Bitly failure")
        print(response.json())

if __name__ == "__main__":

    link = 'https://www.scotthyoung.com/blog/2021/04/12/help-me-with-my-new-project/'
    msg = 'Check out'
    post_on = {
        'twitter': False,
        'reddit': [], # insert subreddits list
    }

    short_url = shorten_url(link)
    if post_on['twitter']:
        tweet(msg + ' ' + short_url)
    if len(post_on['reddit']) > 0:
        post_on_reddit(post_on['reddit'], msg, link)