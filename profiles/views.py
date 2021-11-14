from django.shortcuts import render
from orders.models import order
# from .forms import register_form
from .models import user_profile
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your views here.
def order_view(request):
    us = user_profile.objects.all().filter(name = request.user).first()
    qs = order.objects.all().filter(user = us)
    qs1 = qs.filter(r_status = "Placed")    
    qs2 = qs.filter(r_status = "Using")    
    qs3 = qs.filter(r_status = "Returned")

    no_use, no_ret = 1, 1
    if len(qs2):
        no_use = 0
    if len(qs3):
        no_ret = 0

    temp = 50
    
    return render(request, "profiles/profile.html", 
    {"qs1":qs1, "qs2":qs2, "qs3":qs3, "no_use":no_use, "no_ret":no_ret, "test":temp, "u":us})


from django.contrib.auth import get_user_model
User = get_user_model()

# @receiver(post_save, sender = User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         # UserProfile.objects.create(user=instance)
#         # EmailAdress.objects.create(user_id = instance.id, user_email=instance.email)
#         # print("*******************")
#         # print(instance, instance.username, instance.password)
#         # print("!!!!!!!!!!!!!!!!!!!")
#         # print(sender)
#         # try:
#         #     print("$$$$$$", instance.email)
#         # except:
#         #     print("^^^^^^")

#         # if instance.email == '':
#         #     email = "No email linked with this account"

#         user.objects.create(username = instance.username, email = instance.email, pswd = instance.password)