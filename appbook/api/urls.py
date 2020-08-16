from django.conf.urls import url
from .views import UserListAPIView

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$',UserListAPIView.as_view(),name='list'),#/api/user/
]