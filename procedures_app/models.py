from django.db import models

class MyUser(models.Model):
    name = models.CharField(verbose_name="Пользователь", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
