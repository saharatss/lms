# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.utils import timezone

from django.forms import ModelForm
from adddata.models import User

class Post(models.Model):
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

class SDetail(models.Model):
    textType= models.IntegerField()
    text    = models.CharField(max_length=100000)

class Chapter(models.Model):
    title   = models.CharField(max_length=200)
    detail = models.ForeignKey(SDetail)
    author  = models.ForeignKey('auth.User')
    publish = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Lesson(models.Model):
    title   = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter)

class Subject(models.Model):
    title   = models.CharField(max_length=200)
    lesson  = models.ForeignKey(Lesson)

class Class(models.Model):
    title   = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject)
