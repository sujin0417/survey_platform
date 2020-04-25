from django.db import models

# Create your models here.

class Answer(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='사용자')
    problem = models.ForeignKey(
        'problem.Problem', on_delete=models.CASCADE, verbose_name='문제')
    answer = models.TextField(verbose_name="답")
    ans_valid = models.IntegerField(verbose_name="사용가능 여부")


    def __str__(self):
        return str(self.user) + ' ' + str(self.problem)

    class Meta:
        db_table = 'answer'
        verbose_name = '답변'
        verbose_name_plural = '답변'