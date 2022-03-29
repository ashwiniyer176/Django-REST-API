from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# A Serializer is a Form, therefore a ModelSerializer is essentially a ModelForm


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializers provide a way of serializing and deserializing the snippet
    instances into representations such as json, which work similar to
    Django's forms.
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="snippet-detail",
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
