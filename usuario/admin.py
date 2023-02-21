from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin', 'username', 'active', 'staff' ]
    list_filter = ['admin','username','staff', 'active',]
    fieldsets = (
        (None, {'fields': ('username','email')}),
        ('Permissões', {'fields': ('admin','staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password_2')}
        ),
    )
    search_fields = ['username', 'email', 'staff', 'active', ]
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

