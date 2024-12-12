from celery import shared_task
from .utils import fetch_twitter_data, fetch_facebook_data

@shared_task
def update_social_data(user_id):
    from users.models import Profile
    user = Profile.objects.get(user__id=user_id)
    twitter_data = fetch_twitter_data(user)
    facebook_data = fetch_facebook_data(user)
    # Save data to the database or cache as needed
