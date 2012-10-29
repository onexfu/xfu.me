from django.conf.urls.defaults import patterns, url


from views import BackendView


urlpatterns = patterns('',
	
	url(r'^$', BackendView.as_view(), name='index'),
	


)
