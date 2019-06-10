from django.db import models

# Create your models here.

class UserLogin(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now=True)
    username = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    class Meta:
        verbose_name = "userLogin"
        verbose_name_plural = "usersLogin"
 
    def __unicode__(self):
        return self.name


class ShopDetails(models.Model):
    about_us = models.TextField(max_length=300)
    address1 = models.TextField(max_length=250)
    address2 = models.TextField(max_length=250,blank=True)
    phone_number1 = models.TextField(max_length=200,blank=True)
    phone_number2 = models.TextField(max_length=200,blank=True)
    email = models.EmailField(max_length=50)
    timing = models.TextField(max_length=150)
    facebook_link = models.TextField(max_length=150)
    twitter_link = models.TextField(max_length=150)
    shop_name = models.TextField(max_length=150)
    address1_latitude = models.TextField(max_length=50,blank=True)
    address1_longitude = models.TextField(max_length=50,blank=True)
    address2_latitude = models.TextField(max_length=50,blank=True)
    address2_longitude = models.TextField(max_length=50,blank=True)
    class Meta:
        verbose_name = "ShopDetail"
        verbose_name_plural = "ShopDetails"
 
    def __unicode__(self):
        return self.name


class FeedBackDetails(models.Model):
    name = models.TextField(max_length=100)
    customer_mail = models.EmailField(max_length=100)
    customer_phone = models.TextField(max_length=20,blank=True)
    subject = models.TextField(max_length=250,blank=True)
    message = models.TextField(max_length=200,blank=True)
    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "listOfFeedback"
    def __unicode__(self):
        return self.name

#login_id = models.AutoField(primary_key=True)
    