from django import forms

from posts.models import Hashtag

HASHTAG_CHOICES = (
    (hashtag.id, hashtag.title) for hashtag in Hashtag.objects.all()
)


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=15, min_length=5)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    hashtag = forms.ChoiceField(choices=HASHTAG_CHOICES)

class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Leave a comment')
