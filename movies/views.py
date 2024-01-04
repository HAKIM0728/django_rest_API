from django.http import HttpResponse
from django.shortcuts import render
data={
    'movies':[{
    'ID':1,
    'NAME':'PATEL DIP',
    'YOB':2001
    },
    {
    'ID':2,
    'NAME':'DHAVAL VANARA',
    'YOB':1998
    },
    {
    'ID':3,
    'NAME':'HAKIMALI DATARDI',
    'YOB':2000}]

    }
def movies(request):
    return render(request,'movies/movies.html',data)

def homepage(request):
    return HttpResponse("<h1>HOMEPAGE<h1>")

