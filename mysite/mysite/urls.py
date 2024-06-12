from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("polls/", include("polls.urls")), #always use include when you include other URL patterns. admin.site.urls is the only option to this
    path("admin/", admin.site.urls),
]
