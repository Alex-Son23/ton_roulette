from django.db import models
from django.core.exceptions import ValidationError
from asgiref.sync import sync_to_async


class Draw(models.Model):
    winning_name   = models.CharField(max_length=255)
    win_percentage = models.FloatField(default=0)   # шанс выпадения, %
    dis_percentage = models.FloatField(default=0)   # скидка/бонус (что показываем как "бонус: X%")

    # НОВОЕ: диапазоны TON
    min_amount = models.FloatField(default=0.0)
    max_amount = models.FloatField(default=999999.0)

    # НОВОЕ: ссылка на пост “Все подарки”
    gifts_link = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "draw"   # ВАЖНО: то же имя, что у SQLAlchemy-модели
        verbose_name = "Приз"
        verbose_name_plural = "Призы"

    def clean(self):
        # Базовая валидация диапазона
        if self.min_amount < 0 or self.max_amount <= self.min_amount:
            raise ValidationError("Проверьте корректность диапазона: min_amount < max_amount и min_amount ≥ 0.")

        # (Опционально) Проверка пересечений диапазонов с другими записями
        qs = Draw.objects.exclude(pk=self.pk)
        overlapping = qs.filter(
            min_amount__lte=self.max_amount,
            max_amount__gte=self.min_amount,
        ).exists()
        # Если НЕ хотите запрещать пересечения — закомментируйте блок ниже
        # if overlapping:
        #     raise ValidationError("Диапазон пересекается с уже существующим. Уточните границы.")
    
    def __str__(self):
        return f"{self.winning_name} [{self.min_amount}–{self.max_amount}]"


class GlobalPrompt(models.Model):
    prompt_text = models.TextField("Текст промпта")

    def save(self, *args, **kwargs):
        # Гарантия единственного экземпляра
        if not self.pk and GlobalPrompt.objects.exists():
            raise ValueError("Может существовать только один глобальный промпт")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.prompt_text[:50] + "..." if len(self.prompt_text) > 50 else self.prompt_text
    
    @classmethod
    async def aget_prompt(cls):
        # Возвращает единственный промпт (если он есть)
        return await sync_to_async(cls.objects.first)()

    class Meta:
        verbose_name = "Глобальный промпт"
        verbose_name_plural = "Глобальный промпт"