from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy as _
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Bank, Account, DestinationCategory, Destination, Release, Payment, FormPayment
from .forms import AccountForm


success_url_bank = _('financial:bank_list')
success_url_account = _('financial:account_list')
success_url_release = _('financial:release_list')
success_url_destcat = _('financial:destcat_list')
success_url_destination = _('financial:destcat_list')
success_url_formpay = _('financial:formpay_list')
success_url_payment = _('financial:payment_list')



# Bank --------------------------------------------------------------------
class BankList(ListView):
    model = Bank
    template_name = 'financial/bank/bankList.html'

bank_list = BankList.as_view()


class BankCreate(CreateView):
    model = Bank
    template_name = "financial/bank/bankCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_bank

bank_create = BankCreate.as_view()


class BankDetails(DetailView):
    model = Bank
    template_name = "financial/bank/bankDetails.html"

bank_details = BankDetails.as_view()


class BankUpdate(UpdateView):
    model = Bank
    template_name = "financial/bank/bankCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_bank

bank_update = BankUpdate.as_view()


class BankDelete(DeleteView):
    model = Bank
    template_name = "financial/bank/bankDelete.html"
    success_url = success_url_bank

bank_delete = BankDelete.as_view()



# Account -----------------------------------------------------------------
class AccountList(ListView):
    model = Account
    template_name = 'financial/account/accountList.html'

    def get_queryset(self):
        return Account.objects.filter(bank__id=self.kwargs['bank_id'])

    def get_context_data(self, **kwargs):
        context = super(AccountList, self).get_context_data(**kwargs)
        context['bank_id'] = self.kwargs['bank_id']
        context['bank'] = Bank.objects.filter(id=self.kwargs['bank_id'])
        context['bank_name'] = context['bank'][0]
        return context

account_list = AccountList.as_view()


class AccountCreate(CreateView):
    model = Account
    template_name = "financial/account/accountCreateUpdate.html"
    form_class = AccountForm

    def get_context_data(self, **kwargs):
        context = super(AccountCreate, self).get_context_data(**kwargs)
        context['bank_id'] = self.kwargs['bank_id']
        context['bank'] = Bank.objects.filter(id=self.kwargs['bank_id'])
        context['bank_name'] = context['bank'][0]
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bank_id = self.kwargs['bank_id']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return _('financial:account_list', kwargs={'bank_id': self.kwargs['bank_id']})

account_create = AccountCreate.as_view()


class AccountDetails(DetailView):
    model = Account
    template_name = "financial/account/accountDetails.html"
    
    def get_context_data(self, **kwargs):
        context = super(AccountDetails, self).get_context_data(**kwargs)
        context['bank_id'] = self.kwargs['bank_id']
        return context
    
account_details = AccountDetails.as_view()


class AccountUpdate(UpdateView):
    model = Account
    template_name = "financial/account/accountCreateUpdate.html"
    form_class = AccountForm

    def get_context_data(self, **kwargs):
        context = super(AccountUpdate, self).get_context_data(**kwargs)
        context['bank_id'] = self.kwargs['bank_id']
        context['bank'] = Bank.objects.filter(id=self.kwargs['bank_id'])
        context['bank_name'] = context['bank'][0]
        return context
    
    def get_success_url(self):
        return _('financial:account_list', kwargs={'bank_id': self.kwargs['bank_id']})

account_update = AccountUpdate.as_view()


class AccountDelete(DeleteView):
    model = Account
    template_name = "financial/account/accountDelete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bank2'] = Bank.objects.filter(id=self.kwargs['bank_id'])
        context['form'] = AccountForm(self.request.POST or None)
        return context

    def get_success_url(self):
        return _('financial:account_list', kwargs={'bank_id': self.kwargs['bank_id']})

account_delete = AccountDelete.as_view()


# Release------------------------------------------------------------------
class ReleaseList(ListView):
    model = Release
    template_name = 'financial/release/releaseList.html'

release_list = ReleaseList.as_view()


class ReleaseCreate(CreateView):
    model = Release
    template_name = "financial/release/releaseCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_release

release_create = ReleaseCreate.as_view()


class ReleaseDetails(DetailView):
    model = Release
    template_name = "financial/release/releaseDetails.html"

release_details = ReleaseDetails.as_view()


class ReleaseUpdate(UpdateView):
    model = Release
    template_name = "financial/release/releaseCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_release

release_update = ReleaseUpdate.as_view()


class ReleaseDelete(DeleteView):
    model = Release
    template_name = "financial/release/releaseDelete.html"
    success_url = success_url_release

release_delete = ReleaseDelete.as_view()


# Destination Category --------------------------------------------------------
class DestinationCategoryList(ListView):
    model = DestinationCategory
    template_name = 'financial/destination/destCatList.html'

destcat_list = DestinationCategoryList.as_view()


class DestinationCategoryCreate(CreateView):
    model = DestinationCategory
    template_name = "financial/destination/destCatCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_destcat

destcat_create = DestinationCategoryCreate.as_view()


class DestinationCategoryUpdate(UpdateView):
    model = DestinationCategory
    template_name = "financial/destination/destCatCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_destcat

destcat_update = DestinationCategoryUpdate.as_view()


class DestinationCategoryDelete(DeleteView):
    model = DestinationCategory
    template_name = "financial/destination/destCatDelete.html"
    success_url = success_url_destcat

destcat_delete = DestinationCategoryDelete.as_view()


# Destination -----------------------------------------------------------------
class DestinationList(ListView):
    model = Destination
    template_name = 'financial/destination/destinationList.html'

destination_list = DestinationList.as_view()


class DestinationCreate(CreateView):
    model = Destination
    template_name = "financial/destination/destinationCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_destination

destination_create = DestinationCreate.as_view()


class DestinationUpdate(UpdateView):
    model = Destination
    template_name = "financial/destination/destinationCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_destination

destination_update = DestinationUpdate.as_view()


class DestinationDelete(DeleteView):
    model = Destination
    template_name = "financial/destination/destinationDelete.html"
    success_url = success_url_destination

destination_delete = DestinationDelete.as_view()


# FormPayment -------------------------------------------------------------
class FormPaymentList(ListView):
    model = FormPayment
    template_name = 'financial/payment/formPayList.html'

formpayment_list = FormPaymentList.as_view()


class FormPaymentCreate(CreateView):
    model = FormPayment
    template_name = "financial/payment/formPayCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_formpay

formpayment_create = FormPaymentCreate.as_view()


class FormPaymentUpdate(UpdateView):
    model = FormPayment
    template_name = "financial/payment/formPayCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_formpay

formpayment_update = FormPaymentUpdate.as_view()


class FormPaymentDelete(DeleteView):
    model = FormPayment
    template_name = "financial/payment/formPayDelete.html"
    success_url = success_url_formpay

formpayment_delete = FormPaymentDelete.as_view()


# Payment -----------------------------------------------------------------
class PaymentList(ListView):
    model = Payment
    template_name = "financial/payment/paymentList.html"

payment_list = PaymentList.as_view()


class PaymentCreate(CreateView):
    model = Payment
    template_name = "financial/payment/paymentCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_payment

payment_create = PaymentCreate.as_view()


class PaymentDetails(DetailView):
    model = Payment
    template_name = "financial/payment/paymentDetails.html"

payment_details = PaymentDetails.as_view()


class PaymentUpdate(UpdateView):
    model = Payment
    template_name = "financial/payment/paymentCreateUpdate.html"
    fields = '__all__'
    success_url = success_url_payment

Payment_update = PaymentUpdate.as_view()


class PaymentDelete(DeleteView):
    model = Payment
    template_name = "financial/payment/paymentDelete.html"
    success_url = success_url_payment

payment_delete = PaymentDelete.as_view()