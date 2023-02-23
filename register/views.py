from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy as _

from .models import Register



# Register  ----------------------------------------------------------------
class RegisterList(ListView):
    model = Register
    template_name = "register/registerList.html"

register_list = RegisterList.as_view()


class RegisterCreate(CreateView):
    model = Register
    template_name = "register/registerCreateUpdate.html"
    fields = '__all__'
    success_url = _('register:register_list')

register_create = RegisterCreate.as_view()


class RegisterDetails(DetailView):
    model = Register
    template_name = "register/registerDetails.html"

register_details = RegisterDetails.as_view()


class RegisterUpdate(UpdateView):
    model = Register
    template_name = "register/registerCreateUpdate.html"
    fields = '__all__'
    success_url = _('register:register_list')

register_update = RegisterUpdate.as_view()


class RegisterDelete(DeleteView):
    model = Register
    template_name = "register/registerDelete.html"
    success_url = _('register:register_list')

register_delete = RegisterDelete.as_view()