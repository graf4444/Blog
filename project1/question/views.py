from django.shortcuts import render, resolve_url
from django.views.generic import ListView, DetailView, CreateView
from .models import Question
from .forms import QuestionListForm

class QuestionList(ListView):
    model = Question
    template_name = 'question/question_list.html'
    context_object_name = 'question_list'
    
    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionListForm(request.GET)
        self.form.is_valid()
        return super(QuestionList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Question.objects.all()
        if self.form.cleaned_data.get('search'):
            queryset = queryset.filter(question_text__icontains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

class QuestionDetailAjax(DetailView):
    template_name = "question/question_detail_ajax.html"
    model = Question
    context_object_name = "question"

class QuestionDetail(DetailView):
    model = Question
    template_name = 'question/question_detail.html'
    context_object_name = 'question'
    
class QuestionCreate(CreateView):
    model = Question
    template_name = 'question/create.html'
    fields = ['question_text', 'category']

#    def dispatch(self, request, *args, **kwars):
#        self.form = QuestionForm(request.POST)
#        self.form.is_valid()
#        return super(QuestionCreate, self).dispatch(request, *args, **kwargs)

#    def get_context_data(self, **kwargs):
#        context = super(QuestionCreate, self).get_context_data(**kwargs)
#        context['form'] = self.form
#        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('core:question:question_detail', pk=self.object.pk)
