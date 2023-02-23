from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('financial/', include('financial.urls'), name='financial'),
    path('order/', include('order.urls'), name='order'),
    path('product/', include('product.urls'), name='product'),
    path('register/', include('register.urls'), name='register')
]


