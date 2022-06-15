import imp
from django import forms
from django.contrib.gis import forms
from .models import Post
class PostForm(forms.Form):
    location = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    class Meta:
        models = Post
        fields = ('name','comment',)