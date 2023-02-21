from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy as _
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Bank, Account, Release, ExpenseCategory, Expense



# Bank --------------------------------------------------------------------
class BankList(ListView):
    model = Bank
    template_name = 'financial/bank/bankList.html'

bank_list = BankList.as_view()


class BankRegister(CreateView):
    model = Bank
    template_name = "financial/bank/bankRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:bank_list')

bank_register = BankRegister.as_view()


class BankDetails(DetailView):
    model = Bank
    template_name = "financial/bank/bankDetails.html"

bank_details = BankDetails.as_view()


class BankUpdate(UpdateView):
    model = Bank
    template_name = "financial/bank/bankRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:bank_list')

bank_update = BankUpdate.as_view()


class BankDelete(DeleteView):
    model = Bank
    template_name = "financial/bank/bankDelete.html"
    success_url = _('financial:bank_list')

bank_delete = BankDelete.as_view()



# Account -----------------------------------------------------------------
class AccountList(ListView):
    model = Account
    template_name = 'financial/account/accountList.html'

account_list = AccountList.as_view()


class AccountRegister(CreateView):
    model = Account
    template_name = "financial/account/accountRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:account_list')

account_register = AccountRegister.as_view()


class AccountDetails(DetailView):
    model = Account
    template_name = "financial/account/accountDetails.html"

account_details = AccountDetails.as_view()


class AccountUpdate(UpdateView):
    model = Account
    template_name = "financial/account/accountRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:account_list')

account_update = AccountUpdate.as_view()


class AccountDelete(DeleteView):
    model = Account
    template_name = "financial/account/accountDelete.html"
    success_url = _('financial:account_list')

account_delete = AccountDelete.as_view()


# Release------------------------------------------------------------------
class ReleaseList(ListView):
    model = Release
    template_name = 'financial/release/releaseList.html'

release_list = ReleaseList.as_view()


class ReleaseRegister(CreateView):
    model = Release
    template_name = "financial/release/releaseRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:release_list')

release_register = ReleaseRegister.as_view()


class ReleaseDetails(DetailView):
    model = Release
    template_name = "financial/release/releaseDetails.html"

release_details = ReleaseDetails.as_view()


class ReleaseUpdate(UpdateView):
    model = Release
    template_name = "financial/release/releaseRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:release_list')

release_update = ReleaseUpdate.as_view()


class ReleaseDelete(DeleteView):
    model = Release
    template_name = "financial/release/releaseDelete.html"
    success_url = _('financial:release_list')

release_delete = ReleaseDelete.as_view()


# Expense Category --------------------------------------------------------
class ExpenseCategoryList(ListView):
    model = ExpenseCategory
    template_name = 'financial/expense/expensecategoryList.html'

expensecategory_list = ExpenseCategoryList.as_view()


class ExpenseCategoryRegister(CreateView):
    model = ExpenseCategory
    template_name = "financial/expense/expensecategoryRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:expensecategory_list')

expensecategory_register = ExpenseCategoryRegister.as_view()


class ExpenseCategoryUpdate(UpdateView):
    model = ExpenseCategory
    template_name = "financial/expense/expensecategoryRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:expensecategory_list')

expensecategory_update = ExpenseCategoryUpdate.as_view()


class ExpenseCategoryDelete(DeleteView):
    model = ExpenseCategory
    template_name = "financial/expense/expensecategoryDelete.html"
    success_url = _('financial:expensecategory_list')

expensecategory_delete = ExpenseCategoryDelete.as_view()


# Expense -----------------------------------------------------------------
class ExpenseList(ListView):
    model = Expense
    template_name = 'financial/expense/expenseList.html'

expense_list = ExpenseList.as_view()


class ExpenseRegister(CreateView):
    model = Expense
    template_name = "financial/expense/expenseRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:expense_list')

expense_register = ExpenseRegister.as_view()


class ExpenseUpdate(UpdateView):
    model = Expense
    template_name = "financial/expense/expenseRegisterUpdate.html"
    fields = '__all__'
    success_url = _('financial:expense_list')

expense_update = ExpenseUpdate.as_view()


class ExpenseDelete(DeleteView):
    model = Expense
    template_name = "financial/expense/expenseDelete.html"
    success_url = _('financial:expense_list')

expense_delete = ExpenseDelete.as_view()