from django.urls import path

from . import views as v


app_name = "order"


urlpatterns = [
    # Order ---------------------------------------------------------------------
    path('', v.order_list, name='order_list'),
    path('create/', v.order_create, name='order_create'),
    path('<int:pk>/details/', v.order_details, name='order_details'),
    path('<int:pk>/update/', v.order_update, name='order_update'),
    path('<int:pk>/delete/', v.order_delete, name='order_delete'),
]