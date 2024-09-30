from django.db import models
from oscarbot.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'{self.user} {self.date}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
