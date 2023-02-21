from django.urls import path

from .views import RegisterView


app_name = 'usuario'


urlpatterns = [
    path('cadastrar/', RegisterView.as_view(), name='signup'),
]



    