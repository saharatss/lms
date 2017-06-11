from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Class', 'subject',)

class myForm(forms.Form):
    Class           = forms.CharField(max_length=200)
    subject         = forms.CharField(max_length=200)
    lesson          = forms.CharField(max_length=200)
    chapter         = forms.CharField(max_length=200)
    detail          = forms.CharField()
    publish         = forms.BooleanField(required=False,initial=False, label='Extra cheeze') 