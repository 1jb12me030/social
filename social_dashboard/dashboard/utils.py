import requests

def fetch_twitter_data(user):
    url = "https://api.twitter.com/2/me"
    headers = {
        "Authorization": f"Bearer {user.profile.twitter_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def fetch_facebook_data(user):
    url = f"https://graph.facebook.com/v11.0/me?fields=id,name,posts&access_token={user.profile.facebook_token}"
    response = requests.get(url)
    return response.json()
