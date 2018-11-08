from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('user_management.avatar.urls.profile_avatar')),
    url(r'', include('user_management.avatar.urls.user_avatar')),
]
