from django.conf.urls.defaults import patterns

urlpatterns = patterns('invcode.views',
    (r'^$', 'index'),
)

