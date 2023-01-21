from django.shortcuts import render, HttpResponse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def cats(request, catid=False):
    if request.GET:
        print(request.GET)
    if not catid:
        return HttpResponse('Страница котиков без ID')
    else:
        return HttpResponse(f'Страница котиков {catid}')
