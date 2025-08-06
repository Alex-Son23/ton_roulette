from django.contrib import admin
from .models import Draw

@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display  = ("winning_name", "win_percentage", "dis_percentage",
                     "min_amount", "max_amount", "gifts_link")
    list_filter   = ("min_amount", "max_amount")
    search_fields = ("winning_name",)
    ordering      = ("min_amount", "max_amount", "winning_name")
    fieldsets = (
        (None, {
            "fields": ("winning_name", "dis_percentage", "win_percentage")
        }),
        ("Диапазон TON", {
            "fields": ("min_amount", "max_amount")
        }),
        ("Ссылка", {
            "fields": ("gifts_link",),
            "description": 'Ссылка на пост со списком всех подарков. В сообщении бот добавит якорь <b>«Все подарки»</b>.'
        }),
    )
