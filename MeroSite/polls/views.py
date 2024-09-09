from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world, you are at the polls index")


def detail(request, question_id):
    return HttpResponse("You are looking at a question %s." % question_id)

def results(request, question_id):
    response = "you are looking at the response of the questions %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on the question %s" % question_id)
