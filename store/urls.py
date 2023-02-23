from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('', include('financial.urls'), name='financial'),
    path('', include('order.urls'), name='order'),
    path('', include('product.urls'), name='product'),
    path('', include('register.urls'), name='register')
]


