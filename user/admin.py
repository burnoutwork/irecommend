from django.contrib import admin

from .models import Worker, Business


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'id')
    exclude = ('password',)


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'id')
    exclude = ('password',)
