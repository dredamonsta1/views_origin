from __future__ import unicode_literals

from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, post):
        user_list = User.objects.filter(email=post['email'])
        if user_list:
            user = user_list[0]
            if bcrypt.hashpw(post['password'].encode(), user.password.encode()) == user.password:
                return user
        return None

def register(self, post):
        encrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
        user.objects.create(first_name=post['first_name'], last_name=post['last_name'], email=post['email'], password=encrypted_password)
        return new_user

def validate_user_info(self, post):
        errors = []

        if len(post['first_name']) ==0:
            errors.append("First Name is required")
        elif len(post['first_name']) < 2:
            errors.append("First Name must be at least 2 characters")
        elif not post['first_name'].isalpha():
            errors.append("Only letters HAHAHA ")

        if len(post['last_name']) ==0:
            errors.append("Last Name is required")
        elif len(post['last_name']) < 2:
            errors.append("Last Name must be at least 2 characters")
        elif not post['last_name'].isalpha():
            errors.append("Only letters HAHAHA ")

        if len(post['email']) == 0:
            errors.append("Email please")
        elif not EMAIL_REGEX.match(post['email']):
            errors.append("Cmon Brooo")
        if len(post['password']) == 0:
            errors.append("password is required")
        elif len(post['password']) < 8:
            errors.append("password must be atleast 8 characters long")
        elif post['password'] != post['passconf']:
            errors.append("password and confirmation fields must match")
        if len(User.objects.filter(email=post['email'])) > 0:
            errors.append("Email address is unavailable!")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updted_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
