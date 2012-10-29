from django.views.generic import (ListView, DetailView, CreateView,
	UpdateView)
from django.core.urlresolvers import reverse_lazy


from xfume.uas.views import LoginRequiredMixin
from xfume.common.views import DeleteSingleObject
from utils import Gallery


# db
from models import Template, TemplateForm



detail_template_name = 'ebay_templater/detail.html'


class TemplateList(LoginRequiredMixin, ListView):
	queryset = Template.objects.order_by('-created')
	template_name = 'ebay_templater/index.html'


class CreateTemplate(LoginRequiredMixin, CreateView):
	model = Template
	form_class = TemplateForm
	success_url = reverse_lazy('templater:index')
	template_name = detail_template_name

	def get_context_data(self, **kwargs):
		ctx = super(self.__class__, self).get_context_data(**kwargs)
		ctx['is_create'] = True
		return ctx

class UpdateTemplate(LoginRequiredMixin, UpdateView):
	model = Template
	form_class = TemplateForm
	success_url = reverse_lazy('templater:index')
	template_name = detail_template_name

	def get_context_data(self, **kwargs):
		ctx = super(self.__class__, self).get_context_data(**kwargs)
		ctx['is_create'] = False
		return ctx


class DeleteTemplate(DeleteSingleObject):
	model = Template
	success_url = reverse_lazy('templater:index')


class ViewTemplate(LoginRequiredMixin, DetailView):
	"""
	To generate ebay templates
	"""
	model = Template
	template_name ='ebay_templater/template.html'

	def get_context_data(self, **kwargs):
		ctx = super(self.__class__, self).get_context_data(**kwargs)
		gallery = Gallery(self.object.album_name, '128')
		ctx['gallery'] = gallery.build()
		return ctx



		

		
		
		
		
		
		
