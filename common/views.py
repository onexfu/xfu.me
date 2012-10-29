from django.views.generic import DeleteView

from xfume.uas.views import LoginRequiredMixin
from forms import ObjectDeleteForm



class DeleteSingleObject(LoginRequiredMixin, DeleteView):
    model = None
    success_url = None
    template_name = 'common/confirm_delete.html'


    def get_context_data(self, **kwargs):
        ctx = super(DeleteSingleObject, self).get_context_data(**kwargs)
        ctx['form'] = ObjectDeleteForm(cancel_url=self.success_url)
        return ctx