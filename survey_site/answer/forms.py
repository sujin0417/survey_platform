from django import forms
from .models import Answer
from problem.models import Problem
from user.models import User

class AnswerForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    answer = forms.CharField(
        error_messages={
            'required': '답을 입력해주세요.'
            }, label='answer'
    )
    problem = forms.IntegerField(
        error_messages={
            'required':'문제를 입력해주세요.'
        }, label='문제', widget=forms.HiddenInput
    )
    

    def clean(self):
        cleaned_data = super().clean()
        answer = cleaned_data.get('answer')
        problem = cleaned_data.get('problem')
        user = self.request.session.get('assigned_id')
        if len(str(answer))<50:
           ans_valid = 0
        else:
           ans_valid = 1

        answer = Answer(
                answer = answer,
                problem = Problem.objects.get(pk=problem),
                user = User.objects.get(assigned_id=user),
                ans_valid = ans_valid
            )
        answer.save()


        