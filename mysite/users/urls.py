from django.conf.urls import url

urlpatterns = [
    url(r'^login', 'users.views.user_login'),
    url(r'^logout', 'users.views.user_logout'),
    url(r'^register', 'users.views.user_register'),
]