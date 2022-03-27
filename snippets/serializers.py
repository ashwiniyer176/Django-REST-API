from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# A Serializer is a Form, therefore a ModelSerializer is essentially a ModelForm


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializers provide a way of serializing and deserializing the snippet
    instances into representations such as json, which work similar to
    Django's forms.
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style", "owner"]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
