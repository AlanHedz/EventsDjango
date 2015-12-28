from django.contrib import admin
from .models import User
from .actions import export_xls


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'email')
	search_fields = ('username', 'email')
	list_filter = ('is_superuser',)
	ordering = ('username',)
	filter_horizontal= ('groups', 'user_permissions')
	actions = [export_xls]

	fieldsets = (
			('User', {'fields': ('username', 'password')}),
			('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
			('Permissions', {'fields': ('is_activate', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		)
