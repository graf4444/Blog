from django.shortcuts import render, resolve_url

from .models import Answer
from question.models import Question
from django.views.generic import CreateView

class AnswerCreate(CreateView):
    model = Answer
    template_name = 'answer/create.html'
    fields = ['text']

    def form_valid(self, form):
        print("!!", self.kwargs['question_id'])
        form.instance.autor = self.request.user
        form.instance.question = Question.objects.get(pk=self.kwargs['question_id'])
        return super(AnswerCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('core:question:question_detail', pk=Question.objects.get(pk=self.kwargs['question_id']).pk)
