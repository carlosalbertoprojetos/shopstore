from django.views.generic import CreateView


from .forms import  RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/signup.html'
    success_url = '/'

signup = RegisterView.as_view()