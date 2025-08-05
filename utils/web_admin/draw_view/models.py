from django.db import models


class Draw(models.Model):
    class Meta:
        db_table = "draw"
        verbose_name = "Розыгрыш"
        verbose_name_plural = "Розыгрыш"

    id = models.AutoField('ID', primary_key=True)
    winning_name = models.TextField('Название выигрыша')
    win_percentage = models.FloatField('Поцент выигрыша')
    dis_percentage = models.FloatField('Отображаемый процент')

    def __str__(self):
        return f"{self.id}"
