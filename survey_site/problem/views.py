from django.shortcuts import render
from django.views.generic import DetailView
from .models import Problem
from answer.forms import AnswerForm

# Create your views here.

class Problem_Ans(DetailView):
    template_name = 'problem_ans.html'
    queryset=Problem.objects.all()
    context_object_name='problem'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm(self.request)
        return context
    



    