from django.shortcuts import render
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import user_profile
from django.contrib.auth import get_user_model
User = get_user_model()
