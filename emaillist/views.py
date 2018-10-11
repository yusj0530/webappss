from django.http import  HttpResponseRedirect
from django.shortcuts import render
from emaillist import models
# Create your views here.

def index(request):
    results = models.fetchall()
    data = {'emaillist_list' : results}
    #data는 딕셔러니로 받아온다.
    #랜더링은 html로 바꾸는 과정이다.
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    #form.html에가서 각 name을 확인해서 넣어준다.
    first_name = request.POST['fn']
    last_name = request.POST['ln']
    email = request.POST['email']

    models.insert((first_name, last_name, email))

    return HttpResponseRedirect("/emaillist")