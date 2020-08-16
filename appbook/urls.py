from django.conf.urls import url
from .views import UserListView
# from .views import tweet_detail_view,tweet_list_view
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^$',tweet_list_view,name='list'),
    # url(r'^1/$',tweet_detail_view,name='detail'),
    # url(r'^(?P<pk>\d+)/$',tweet_detail_view,name='detail'),
    
    url(r'^search/$',UserListView.as_view(),name='list'),
]