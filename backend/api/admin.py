from django.contrib import admin

# Register your models here.

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff']
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )
admin.site.register(User, UserAdmin)