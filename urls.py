from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # backend
    (r'^backend/', include('xfume.backend.urls', namespace="backend")),

    # ebay_templater
	(r'^templater/', include('xfume.ebay_templater.urls', namespace="templater")),

    # uas
    (r'^uas/', include('xfume.uas.urls', namespace="uas")),

    # readlinglist
    (r'^readling-list/', include('xfume.readinglist.urls', namespace="rlist")),


	(r'^$', TemplateView.as_view(template_name='index.html')),



	#(r'^backend/$', TemplateView.as_view(template_name='base_backend.html')),


)






#------- serving local deployment files ----------------
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.MEDIA_ROOT,
    }),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.STATIC_ROOT,
    }),
)





