from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'birthday', 'bio', 'location', 'is_online', 'last_visited', 'photo')
    list_display = ( 'id', 'username', 'first_name', 'last_name',)
    list_filter = ('username',)
    search_fields = ('username',)
admin.site.register(User, UserAdmin)
# Register your models here.
