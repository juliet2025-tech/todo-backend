from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import update_last_login

@receiver(user_logged_in)
def update_last_login_signal(sender, request, user, **kwargs):
    """
    This signal updates the last_login field automatically
    whenever a user successfully logs in.
    """
    update_last_login(None, user)