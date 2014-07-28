from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns(
    '',
    url(
        r'^user/(?P<slug>[a-zA-Z-_0-9]+)/$',
        UserDetailView.as_view(),
        name="user-detail"
    ),
    url(
        r'^user/(?P<slug>.*)/update/$',
        UserUpdateView.as_view(),
        name="user-update"
    ),
    url(
        r'^user-create/$',
        UserCreateView.as_view(),
        name="user-create"
    ),
)