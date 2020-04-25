from django.contrib import admin
from .models import Answer

# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'problem')


admin.site.register(Answer, AnswerAdmin)
