from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.CharField(verbose_name="title", max_length=128)
    instruction = models.TextField(verbose_name="질문 내용")
    visualization = models.TextField(verbose_name="시각화")

    def __str__(self):
        return str(self.id) +' '+ str(self.title)

    class Meta:
        db_table = 'problem'
        verbose_name = '문제'
        verbose_name_plural = '문제'