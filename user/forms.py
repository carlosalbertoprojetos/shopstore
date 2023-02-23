from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# User = get_user_model()

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password_2',]

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Este usuário já está sendo utilizado")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("Este email já está sendo utilizado")
#         return email

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "As senhas precisam ser iguais.")
#         return cleaned_data


# class UserAdminCreationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = [ 'username', 'email',]

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "As senhas precisam ser iguais.")
#         return cleaned_data

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class UserAdminChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'staff', 'active', 'admin',]

#     def clean_password(self):
#         return self.initial["password"]


