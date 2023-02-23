from django.urls import path

from . import views as v


app_name = "product"


urlpatterns = [
    # Unit Measure ------------------------------------------------------------
    path('unitmeasure/', v.unitmeas_list, name='unitmeas_list'),
    path('unitmeasure/create/', v.unitmeas_create, name='unitmeas_create'),
    path('unitmeasure/<int:pk>/update/', v.unitmeas_update, name='unitmeas_update'),
    path('unitmeasure/<int:pk>/delete/', v.unitmeas_delete, name='unitmeas_delete'),

    # Product Category --------------------------------------------------------
    path('category/', v.prodcat_list, name='prodcat_list'),
    path('category/create/', v.prodcat_create, name='prodcat_create'),
    path('category/<int:pk>/update/', v.prodcat_update, name='prodcat_update'),
    path('category/<int:pk>/delete/', v.prodcat_delete, name='prodcat_delete'),

    # Product -----------------------------------------------------------------
    path('', v.product_list, name='product_list'),
    path('create/', v.product_create, name='product_create'),
    path('<int:pk>/details/', v.product_details, name='product_details'),
    path('<int:pk>/update/', v.product_update, name='product_update'),
    path('<int:pk>/delete/', v.product_delete, name='product_delete'),
]