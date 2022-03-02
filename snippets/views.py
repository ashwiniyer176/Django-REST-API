from django.http import Http404

from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

"""
Views here can be:

1. Functions: These are made using the @api_view decorator and are best
suited for single solitary tasks as they can get messy real quick

2. Classes: These are classes inheriting from the APIView class and can
help organize your code in a better manner. By default, this is the most
preferable.

3. Generic Classes: Generic classes are classes which already implement
the most common behaviors. If the choice is between a Class and a 
Generic, always go for a Generic.
"""


class SnippetList(generics.ListCreateAPIView):
    '''
    List all code snippets or create a new snippet
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
