# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from views import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Post._meta.fields]
	#list_editable=("temp","humi")
admin.site.register(Post,PostAdmin)
		