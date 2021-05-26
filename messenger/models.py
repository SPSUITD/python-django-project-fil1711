from django.db import models

class Channel(models.Model):
  title = models.CharField(max_length=200)

class Message(models.Model):
  author = models.CharField(max_length=200)
  channel = models.CharField(max_length=200)
  text = models.CharField(max_length=1000)
  pub_date = models.DateTimeField(auto_now_add=True)
