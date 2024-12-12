import requests

def fetch_twitter_data(user):
    try:
        social = user.social_auth.get(provider='twitter')
        access_token = social.extra_data['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get("https://api.twitter.com/2/tweets", headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_facebook_data(user):
    try:
        social = user.social_auth.get(provider='facebook')
        access_token = social.extra_data['access_token']
        url = "https://graph.facebook.com/me?fields=id,name,posts"
        response = requests.get(url, params={'access_token': access_token})
        return response.json()
    except Exception as e:
        return {"error": str(e)}
