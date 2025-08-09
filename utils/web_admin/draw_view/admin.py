from django.contrib import admin
from .models import Draw, GlobalPrompt
from .forms import GlobalPromptForm


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


@admin.register(GlobalPrompt)
class GlobalPromptAdmin(admin.ModelAdmin):
    form = GlobalPromptForm
    list_display = ("short_text",)

    def has_add_permission(self, request):
        # Запрет на добавление, если объект уже есть
        if GlobalPrompt.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        # Если только один промпт, сразу редактируем его
        if GlobalPrompt.objects.count() == 1:
            obj = GlobalPrompt.objects.first()
            return self.change_view(request, str(obj.id))
        return super().changelist_view(request, extra_context)

    def short_text(self, obj):
        return obj.prompt_text[:50] + "..." if len(obj.prompt_text) > 50 else obj.prompt_text
    short_text.short_description = "Текст промпта"