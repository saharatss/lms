from django import forms

from .models import Post ,Document


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
    publish         = forms.CharField(required=False)
    #fields = ('Class','subject','lesson','chapter','detail','publish') 
    #publish         = forms.CharField(required=False) 

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )