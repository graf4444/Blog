from django.shortcuts import render
from django.shortcuts import HttpResponse
from question.models import Question
from answer.models import Answer
from category.models import Category

def index(request):
    latest_categories_list = Category.objects.all()[:5]
    latest_questions_list = Question.objects.all()[:5]
    latest_answers_list = Answer.objects.all()[:5]

    context = {'latest_categories_list': latest_categories_list, 
                'latest_questions_list': latest_questions_list, 
                'latest_answers_list': latest_answers_list}

    return render(request, 'core/index.html', context)
