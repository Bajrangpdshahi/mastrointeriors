# meetdesigner/forms.py
from django import forms
from .models import BlogPost


class MeetDesignerForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']  # Include the image field
        widgets = {
            'content': forms.Textarea(attrs={'id': 'editor'}),
        }

