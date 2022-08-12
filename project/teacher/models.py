import imp
from tkinter import CASCADE
from django.db import models
from classes.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class teacher(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='post_images', default="profile.png")
    myclasses = models.ManyToManyField(Classes)

    def __str__(self):
        return self.name.username