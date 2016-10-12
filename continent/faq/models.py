from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    ansver = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question
