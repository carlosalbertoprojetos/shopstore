from django.urls import path

from . import views as v


app_name = "register"


urlpatterns = [
    # Register ----------------------------------------------------------------
    path('', v.register_list, name='register_list'),
    path('create/', v.register_create, name='register_create'),
    path('<int:pk>/details/', v.register_details, name='register_details'),
    path('<int:pk>/update/', v.register_update, name='register_update'),
    path('<int:pk>/delete/', v.register_delete, name='register_delete'),
]