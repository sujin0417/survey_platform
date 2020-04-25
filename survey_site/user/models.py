import uuid
from django.db import models

# Create your models here.

class User(models.Model):
    assigned_id = models.UUIDField(
        max_length=32, verbose_name="할당 아이디", default=uuid.uuid4, editable=False,unique=True)
    finished_code = models.CharField(
        max_length=32, verbose_name="Finished_code", default='0')

    def __str__(self):
        return str(self.id)+' '+str(self.assigned_id)

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'