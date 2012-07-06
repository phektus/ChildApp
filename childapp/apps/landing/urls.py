from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('childapp.apps.landing.views',
    url(r'^$', 'index'),
)
