from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'west.views.index'),
    url(r'^staff/', 'west.views.staff'),
    url(r'^template/', 'west.views.templay'),
    url(r'^form/', 'west.views.form'),
]
