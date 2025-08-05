from django.contrib import admin

from .models import Draw


@admin.register(Draw)
class Draw_Admin(admin.ModelAdmin):
    list_display = ("id", "winning_name", "win_percentage", "dis_percentage")
