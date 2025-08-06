from django.contrib import admin

from .models import Log


@admin.register(Log)
class Log_Admin(admin.ModelAdmin):
    list_display = ("id", "amount", "address", "winning_name", "id_trans", "date_register",)
