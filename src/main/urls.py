from django.conf.urls import patterns, url

urlpatterns = patterns(
    'main.views',
    url(r'^$', 'home', {}, 'home'),
    url(r'^store/(?P<store_id>\d+)/$', 'store', name='store'),
)