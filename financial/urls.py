from django.urls import path

from . import views as v


app_name = "financial"


urlpatterns = [
    # Bank --------------------------------------------------------------------
    path('banks/', v.bank_list, name='bank_list'),
    path('bank/register/', v.bank_register, name='bank_register'),
    path('bank/<int:pk>/details/', v.bank_details, name='bank_details'),
    path('bank/<int:pk>/update/', v.bank_update, name='bank_update'),
    path('bank/<int:pk>/delete/', v.bank_delete, name='bank_delete'),


    # Account -----------------------------------------------------------------
    path('account/', v.account_list, name='account_list'),
    path('account/register/', v.account_register, name='account_register'),
    path('account/<int:pk>/details/', v.account_details, name='account_details'),
    path('account/<int:pk>/update/', v.account_update, name='account_update'),
    path('account/<int:pk>/delete/', v.account_delete, name='account_delete'),


    # Release------------------------------------------------------------------
    # path('releases/', v.Lista_LancamentosView.as_view(), name='releases'),


    # Expense Category ------------------------------------------------------
    path('expensive/category/', v.expensecategory_list, name='expensecategory_list'),
    path('expensive/category/register/', v.expensecategory_register, name='expensecategory_register'),
    # path('expensive/category/<int:pk>/details/', v.expensecategory_details, name='expensecategory_details'),
    path('expensive/category/<int:pk>/update/', v.expensecategory_update, name='expensecategory_update'),
    path('expensive/category/<int:pk>/delete/', v.expensecategory_delete, name='expensecategory_delete'),


    # Expense ---------------------------------------------------------------
    path('expensive/', v.expense_list, name='expense_list'),
    path('expensive/register/', v.expense_register, name='expensive_register'),
    # path('expensive/<int:pk>/details/', v.expensive_details, name='expensive_details'),
    path('expensive/<int:pk>/update/', v.expense_update, name='expensive_update'),
    path('expensive/<int:pk>/delete/', v.expense_delete, name='expensive_delete'),

]



