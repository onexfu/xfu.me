from django.conf.urls.defaults import patterns, url


from views import (TemplateList, CreateTemplate, UpdateTemplate,
	DeleteTemplate, ViewTemplate)


urlpatterns = patterns('',
	
	# template index
	url(r'^$', TemplateList.as_view(), name='index'),
	
	# create
	url(r'^create/$', CreateTemplate.as_view(), name="create"),
	# edit
	url(r'^edit/(?P<pk>\d+)/$', UpdateTemplate.as_view(), name="edit"),
	# delete
	url(r'^delete/(?P<pk>\d+)/$', DeleteTemplate.as_view(), name="delete"),
	
	# view
	url(r'^view_template/(?P<pk>\d+)/$', ViewTemplate.as_view(), name="view"),


)
