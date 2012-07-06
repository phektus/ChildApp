from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('childapp.apps.children.views',
    (r'^new/$', 'edit'),
    (r'^(?P<id>\d+)/$', 'view'),
    (r'^(?P<id>\d+)/edit/$', 'edit'),
    (r'^(?P<id>\d+)/delete/$', 'delete'),
    (r'$', 'index'),
)
