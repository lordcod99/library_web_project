from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=50)
    pswd = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, blank=True, null=True)
    noof_current_books = models.IntegerField(blank=True, null=True)
    n_read = models.IntegerField(blank=True, null=True)
    pic = models.ImageField(blank=True, null=True, upload_to = 'profiles/')

    class Meta:
        managed = False
        db_table = 'user'

class emp(models.Model):
    e_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=50)
    pswd = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'