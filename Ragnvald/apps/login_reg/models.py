from django.db import models
# from apps.process.models import Taskboard, Task

# Create your models here.
class UserManager(models.Manager):
  def is_valid(self, form):
    is_valid = {}
    if len(form['first_name']) < 2:
      is_valid['first_name'] = "Change your first name to be longer."
    if len(form['last_name']) < 2:
      is_valid['last_name'] = "Change your last name to be longer."
    if '@' not in form['email']:
      is_valid['email'] = "Please enter a valid email!"
    if len(User.objects.filter(email=form['email'])) > 0:
      is_valid['email_inuse'] = "Email already in use!"
    if form['password'] != form['confirm_pw'] or len(form['password']) < 7:
      is_valid['password'] = "Password must match and be at least 8 characters."
    return is_valid

class User(models.Model):
  name_first = models.CharField(max_length=255)
  name_last = models.CharField(max_length=255)
  email = models.EmailField()
  date_created = models.DateTimeField(auto_now_add=True)
  password = models.CharField(max_length=255)
  objects = UserManager()