from django.conf.urls.defaults import patterns, url


from views import LoginView, LogoutView


urlpatterns = patterns('',
	
	# login
	url(r'^login/$', LoginView.as_view(), name='login'),

	# logout
	url(r'^logout/$', LogoutView.as_view(), name='logout'),

)
