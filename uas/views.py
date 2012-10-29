from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django import http

from forms import LoginForm



class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url="/uas/login/"))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'uas/login.html'

    def get_success_url(self):
        url = self.request.REQUEST.get('next', None)
        if not url:
            url = reverse('backend:index')
        return url

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(self.__class__, self).form_valid(form)


class LogoutView(View):
    lougout_url = '/'
    
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return http.HttpResponseRedirect(self.lougout_url)



        

        