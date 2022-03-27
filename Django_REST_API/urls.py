from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("snippets.urls")),
]
=======
urlpatterns = [path("admin/", admin.site.urls), path("", include("snippets.urls"))]
>>>>>>> faacbaf05aa659b8b398124dd1a51c9c75d50bb1
