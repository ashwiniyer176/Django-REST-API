from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# A Serializer is a Form, therefore a ModelSerializer is essentially a ModelForm


class SnippetSerializer(serializers.ModelSerializer):
    '''
    Serializers provide a way of serializing and deserializing the snippet 
    instances into representations such as json, which work similar to
    Django's forms. 
    '''
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
