from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
# Create your views here.

def index(request):
    questions = Question.objects.all()
    # html = [question.__str__() for question in questions]
    # #for question in questions:
    #     #html.append("Question is %s" % (question.question_text))
    # return HttpResponse( "<br>".join(html) )
    #return render(request, 'polls/chor.html')
    return render(request, "polls/index.html", {'questions' : questions, 'title' : 'Question '})

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    data = {'question' : question}
    return render(request, 'polls/detail.html', data)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    choice_id = request.POST["choice"]

    selected_choice = question.choice_set.get(pk=choice_id)
    selected_choice.vote += 1
    selected_choice.save()
    return HttpResponseRedirect("/polls/" + str(question_id))
    #question = Question.objects.get(pk = question_id)
