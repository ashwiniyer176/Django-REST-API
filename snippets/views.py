from rest_framework import generics, renderers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides list and retrieve actions
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(self.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )
