from django.views.generic import TemplateView

from xfume.uas.views import LoginRequiredMixin


class BackendView(LoginRequiredMixin, TemplateView):
	template_name = "backend/base.html"


