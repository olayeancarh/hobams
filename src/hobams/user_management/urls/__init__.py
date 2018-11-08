from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('user_management.urls.auth')),
    url(r'', include('user_management.urls.password_reset')),
    url(r'', include('user_management.urls.profile')),
    url(r'', include('user_management.urls.register')),
]
