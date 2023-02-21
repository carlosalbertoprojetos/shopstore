class ExpenseContextDataMixin:
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name.title()
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural.title()  # noqa E501
        context['total'] = sum(self.object_list.values_list('value', flat=True))  # noqa E501
        return context


class ExpenseFormKwargsMixin:

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


        