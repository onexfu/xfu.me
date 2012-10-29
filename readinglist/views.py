from django.views.generic import (ListView, CreateView,
	UpdateView, RedirectView)
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

from xfume.uas.views import LoginRequiredMixin
from xfume.common.views import DeleteSingleObject

# db
from models import ReadingItem, ReadingItemForm





unread_list_url = reverse_lazy('rlist:unread-list')


class AppIndexRedirect(RedirectView):
	url = reverse_lazy('rlist:unread-list')
		

class UnreadList(LoginRequiredMixin, ListView):
	queryset = ReadingItem.objects.filter(is_read=False).order_by('-created_time')
	template_name = 'readinglist/unread-list.html'


class ReadList(LoginRequiredMixin, ListView):
	queryset = ReadingItem.objects.filter(is_read=True).order_by('-read_time')
	template_name = 'readinglist/read-list.html'


class CreateItem(LoginRequiredMixin, CreateView):
	model = ReadingItem
	form_class = ReadingItemForm
	success_url = reverse_lazy('rlist:unread-list')
	template_name = 'readinglist/detail.html'

	def get_context_data(self, **kwargs):
		ctx = super(self.__class__, self).get_context_data(**kwargs)
		ctx['is_create'] = True
		return ctx

class ToReadItem(LoginRequiredMixin, UpdateView):
	model = ReadingItem
	form_class = ReadingItemForm
	success_url = unread_list_url
	template_name = 'readinglist/detail.html'

	def form_valid(self, form):
		if self.request.POST.get('is_read', False):
			form.instance.read_time = timezone.now()
		return super(ToReadItem, self).form_valid(form)

	def get_context_data(self, **kwargs):
		ctx = super(self.__class__, self).get_context_data(**kwargs)
		ctx['is_create'] = False
		return ctx

class DeleteItem(DeleteSingleObject):
	model = ReadingItem
	success_url = unread_list_url
		





