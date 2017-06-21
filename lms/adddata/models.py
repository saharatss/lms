# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.utils import timezone

from django.forms import ModelForm
from adddata.models import User

class DPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    Class           = models.CharField(max_length=200)
    subject         = models.CharField(max_length=200)
    lesson          = models.CharField(max_length=200)
    chapter         = models.CharField(max_length=200)
    detail          = models.TextField()
    author          = models.ForeignKey('auth.User')
    created_date    = models.DateTimeField(default=timezone.now)
    published_date  = models.DateTimeField(blank=True, null=True)
    publish         = models.BooleanField()
    view            = models.IntegerField()
    def publish(self):
        self.published_date = timezone.now()
        self.publish = True
        self.save()


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document    = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
