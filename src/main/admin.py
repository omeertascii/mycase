from django.contrib import admin
from user.models import User

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_staff', 'is_superuser')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    
    admin.site.register(User)