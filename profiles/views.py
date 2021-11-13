from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import user_profile
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        user_profile.objects.create(name = instance.username, email = instance.email, pswd = instance.password)