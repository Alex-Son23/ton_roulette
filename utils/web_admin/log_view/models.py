from django.db import models


class Log(models.Model):
    class Meta:
        db_table = "log"
        verbose_name = "Логи"
        verbose_name_plural = "Логи"

    id = models.AutoField('ID', primary_key=True)
    address = models.TextField('номер кошелька')
    winning_name = models.TextField('Название выигрыша')
    id_trans = models.TextField('id трансакция',null=True,blank=True)
    amount = models.TextField('Диапазон', default="0-0")
    date_register = models.DateTimeField('Дата')

    def __str__(self):
        return f"{self.id}"

