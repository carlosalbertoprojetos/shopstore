from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy as _

from .models import UnitMeasure, ProductCategory, Product



# Unit Measure ------------------------------------------------------------
class UnitMeasList(ListView):
    model = UnitMeasure
    template_name = "product/others/unitmeasList.html"

unitmeas_list = UnitMeasList.as_view()


class UnitMeasCreate(CreateView):
    model = UnitMeasure
    template_name = "product/others/unitmeasCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:unitmeas_list')

unitmeas_create = UnitMeasCreate.as_view()


class UnitMeasUpdate(UpdateView):
    model = UnitMeasure
    template_name = "product/others/unitmeasCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:unitmeas_list')

unitmeas_update = UnitMeasUpdate.as_view()


class UnitMeasDelete(DeleteView):
    model = UnitMeasure
    template_name = "product/others/unitmeasDelete.html"
    success_url = _('product:unitmeas_list')

unitmeas_delete = UnitMeasDelete.as_view()


# Product Category --------------------------------------------------------
class ProductCategoryList(ListView):
    model = ProductCategory
    template_name = "product/others/prodcatList.html"

prodcat_list = ProductCategoryList.as_view()


class ProductCategoryCreate(CreateView):
    model = ProductCategory
    template_name = "product/others/prodcatCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:prodcat_list')

prodcat_create = ProductCategoryCreate.as_view()


class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    template_name = "product/others/prodcatCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:prodcat_list')

prodcat_update = ProductCategoryUpdate.as_view()


class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    template_name = "product/others/prodcatDelete.html"
    success_url = _('product:prodcat_list')

prodcat_delete = ProductCategoryDelete.as_view()


# Product  ----------------------------------------------------------------
class ProductList(ListView):
    model = Product
    template_name = "product/productList.html"

product_list = ProductList.as_view()


class ProductCreate(CreateView):
    model = Product
    template_name = "product/productCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:product_list')

product_create = ProductCreate.as_view()


class ProductDetails(DetailView):
    model = Product
    template_name = "product/productDetails.html"

product_details = ProductDetails.as_view()


class ProductUpdate(UpdateView):
    model = Product
    template_name = "product/productCreateUpdate.html"
    fields = '__all__'
    success_url = _('product:product_list')

product_update = ProductUpdate.as_view()


class ProductDelete(DeleteView):
    model = Product
    template_name = "product/productDelete.html"
    success_url = _('product:product_list')

product_delete = ProductDelete.as_view()
