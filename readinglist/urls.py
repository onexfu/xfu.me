from django.conf.urls.defaults import patterns, url


from views import (AppIndexRedirect, UnreadList, ReadList, 
	CreateItem, ToReadItem, DeleteItem)


urlpatterns = patterns('',

	# redirect
	url(r'^$', AppIndexRedirect.as_view(), name='index'),

	# unread list
	url(r'^unread-list/$', UnreadList.as_view(), name='unread-list'),

	# read list
	url(r'^read-list/$', ReadList.as_view(), name='read-list'),

	# create
	url(r'^create/$', CreateItem.as_view(), name="create"),

	# to read
	url(r'^to_read/(?P<pk>\d+)/$', ToReadItem.as_view(), name="to_read"),

	# delete
	url(r'^delete/(?P<pk>\d+)/$', DeleteItem.as_view(), name="delete"),



)
