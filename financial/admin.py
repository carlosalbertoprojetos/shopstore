from django.contrib import admin

from .models import Bank, Account, Release, ExpenseCategory, Expense



@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    ...


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ...


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    ...


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    ...
