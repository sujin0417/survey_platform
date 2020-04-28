import uuid
import time
import random
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from user.models import User
from problem.models import Problem
from .forms import AnswerForm

# Create your views here.

# 설문 시작 페이지
def start(request):
    assigned_id = uuid.uuid4()
    user = User(
        assigned_id = assigned_id
    )
    user.save()
    assigned_id=str(assigned_id)
    request.session['assigned_id']=assigned_id
    return render(request, 'start.html')
    
# 설문 종료 페이지
def end(request):
    finish_code = str(time.time()).split('.')[0]
    user = User(
        finished_code = finish_code
    )
    user.save()
    del request.session['assigned_id']
    return render(request,'end.html',{'finish_code':finish_code })

# 문제 랜덤 리스트 만들기
def problem_list():
    problem_list=list(Problem.objects.all().values('id'))
    p_index = []
    for i in range(0, len(problem_list)):
        p_index.append(str(problem_list[i]['id'])) 
    p_index = p_index[1:]  
    random.shuffle(p_index)
    return p_index

# 답 적는 폼(problem의 디테일 뷰에서 넘어옴)
class AnswerCreate(FormView):
    form_class = AnswerForm
    success_url = '/problem/2/'

    # if문 리스트에 값이 있을 때 - 다음 인덱스로 이동
    # else 리스트에 값이 없을 때 - 설문 종료

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw