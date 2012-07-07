from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    (r'^children/', include('childapp.apps.children.urls')),
    (r'^', include('childapp.apps.landing.urls')),
)
