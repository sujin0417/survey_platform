import uuid
import time
import random
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from user.models import User
from problem.models import Problem
from .forms import AnswerForm

# Create your views here.


def start(request):
    assigned_id = uuid.uuid4()
    user = User(
        assigned_id = assigned_id
    )
    user.save()
    assigned_id=str(assigned_id)
    request.session['assigned_id']=assigned_id
    problem_list()
    return render(request, 'start.html')
    

def end(request):
    finish_code = str(time.time()).split('.')[0]
    user = User(
        finished_code = finish_code
    )
    user.save()
    del request.session['assigned_id']
    return render(request,'end.html',{'finish_code':finish_code })

def problem_list():
    problem_list=list(Problem.objects.all().values('id'))
    p_index = []
    for i in range(0, len(problem_list)):
        p_index.append(problem_list[i]['id'])   
    random.shuffle(p_index)
    return p_index

class AnswerCreate(FormView):
    form_class = AnswerForm
    success_url = '/problem/2/'
    

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw