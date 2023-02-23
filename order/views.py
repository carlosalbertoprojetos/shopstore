from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy as _


from .models import Order



# Order -------------------------------------------------------------------
class OrderList(ListView):
    model = Order
    template_name = "order/orderList.html"

order_list = OrderList.as_view()


class OrderCreate(CreateView):
    model = Order
    template_name = "order/orderCreateUpdate.html"
    fields = '__all__'
    success_url = _('order:order_list')

order_create = OrderCreate.as_view()


class OrderDetails(DetailView):
    model = Order
    template_name = "order/orderDetails.html"

order_details = OrderDetails.as_view()


class OrderUpdate(UpdateView):
    model = Order
    template_name = "order/orderCreateUpdate.html"
    fields = '__all__'
    success_url = _('order:order_list')

order_update = OrderUpdate.as_view()


class OrderDelete(DeleteView):
    model = Order
    template_name = "order/orderDelete.html"
    success_url = _('order:order_list')

order_delete = OrderDelete.as_view()

