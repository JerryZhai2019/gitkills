from django.http import HttpResponse
from django.shortcuts import redirect
def login(request)
    return redirect('/index')

def index(request):
    return HttpResponse('CSDN读者你们好')
