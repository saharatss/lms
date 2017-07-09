"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from adddata import views ,forms

from django.conf import settings
from django.conf.urls.static import static

#from auth import views ,forms


urlpatterns = [
    # MARK : Authenticate
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^change_password/', views.change_password, name='change_password'),

    url(r'^home/$', views.home, name='home'),
    #url(r'^add/$', views.show_add_page, name='add'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    # MARK : New site
    url(r'^$', views.class_page, name='class_page'),
    url(r'^add/$', views.add_page, name='add_page'),
    url(r'^add-class/$', views.add_class, name='add_class'),
    url(r'^add-detail/$', views.add_detail, name='add_detail'),

    url(r'^test/$', views.simple_upload, name='simple_upload'),                     #simple upload
    url(r'^test2/$', views.model_form_upload, name='model_form_upload'),            #upload connect title to dataBase
    url(r'^test3/$', views.check, name='check'),                                   #test toggle (sliderCheckBox)

    url(r'^signup/$', views.signup, name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)