from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'keep.html',{'title':'Idea Keep'})

def add_item (request):
    return 'yes'