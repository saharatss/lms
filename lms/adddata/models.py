# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from django.utils import timezone


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

class Chapter(models.Model):
    title   = models.CharField(max_length=200)
    detail  = models.CharField(max_length=100000)
    author  = models.ForeignKey('auth.User')
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