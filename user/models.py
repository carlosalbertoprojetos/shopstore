from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager


from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError('Precisa inserir um usuário.')
        if not email:
            raise ValueError('O usuário precisa ter um email válido.')
        if not password:
            raise ValueError('Precisa inserir a senha correta.')

        user_obj = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


    def create_staffuser(self, email, username=None, password=None):
        user = self.create_user(
            email,            
            username=username,
            password=password,
            is_staff=True
        )
        return user


    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            is_staff=True,
            is_admin=True            
        )
        return user


class User(AbstractBaseUser):

    username = models.CharField('Usuário', max_length=255, unique=True)
    email       = models.EmailField('E-mail', unique=True)
    active      = models.BooleanField('Está ativo?', blank=True, default=True)
    staff       = models.BooleanField('É da equipe?', blank=True, default=False)
    admin       = models.BooleanField('Admin?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


    class Meta:
        verbose_name        = 'Usuário'
        verbose_name_plural = 'Usuários'
    

    