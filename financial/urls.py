from django.urls import path

from . import views as v


app_name = "financial"


urlpatterns = [
    # Bank --------------------------------------------------------------------
    path('banks/', v.bank_list, name='bank_list'),
    path('bank/create/', v.bank_create, name='bank_create'),
    path('bank/<int:pk>/details/', v.bank_details, name='bank_details'),
    path('bank/<int:pk>/update/', v.bank_update, name='bank_update'),
    path('bank/<int:pk>/delete/', v.bank_delete, name='bank_delete'),

    # Account ------------------------------------------------------------------
    path('account/', v.account_list, name='account_list'),
    path('account/create/', v.account_create, name='account_create'),
    path('account/<int:pk>/details/', v.account_details, name='account_details'),
    path('account/<int:pk>/update/', v.account_update, name='account_update'),
    path('account/<int:pk>/delete/', v.account_delete, name='account_delete'),

    # Release ------------------------------------------------------------------
    path('release/', v.release_list, name='release_list'),
    path('release/create/', v.release_create, name='release_create'),
    path('release/<int:pk>/details/', v.release_details, name='release_details'),
    path('release/<int:pk>/update/', v.release_update, name='release_update'),
    path('release/<int:pk>/delete/', v.release_delete, name='release_delete'),

    # Destination Category -----------------------------------------------------
    path('destination/category/', v.destcat_list, name='destcat_list'),
    path('destination/category/create/', v.destcat_create, name='destcat_create'),
    path('destination/category/<int:pk>/update/', v.destcat_update, name='destcat_update'),
    path('destination/category/<int:pk>/delete/', v.destcat_delete, name='destcat_delete'),

    # Destination ---------------------------------------------------------------
    path('destination/', v.destination_list, name='destination_list'),
    path('destination/create/', v.destination_create, name='destination_create'),
    path('destination/<int:pk>/update/', v.destination_update, name='destination_update'),
    path('destination/<int:pk>/delete/', v.destination_delete, name='destination_delete'),

    # FormPayment ---------------------------------------------------------------
    path('formpayment/', v.formpayment_list, name='formpayment_list'),
    path('formpayment/create/', v.formpayment_create, name='formpayment_create'),
    path('formpayment/<int:pk>/update/', v.formpayment_update, name='formpayment_update'),
    path('formpayment/<int:pk>/delete/', v.formpayment_delete, name='formpayment_delete'),

    # Payment -------------------------------------------------------------------
    path('payment/', v.payment_list, name='payment_list'),
    path('payment/create/', v.payment_create, name='payment_create'),
    path('payment/<int:pk>/details/', v.payment_details, name='payment_details'),
    path('payment/<int:pk>/update/', v.Payment_update, name='Payment_update'),
    path('payment/<int:pk>/delete/', v.payment_delete, name='payment_delete'),
]