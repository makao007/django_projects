from django.shortcuts import render
from django.shortcuts import redirect

from models import Item as M_Item

import datetime

# Create your views here.
def home (request):

    data = M_Item.objects.all().order_by ('-last_update')

    return render (request, 'keep.html',{'title':'Idea Keep', 'data':data})

def add_item (request):

    if request.method == 'POST':
        xid = request.POST.get('xid',None)
        title = request.POST.get('title','')
        desc = request.POST.get('desc','')

        if xid:
            tmp = M_Item.objects.get(id=int(xid))
            tmp.title = title
            tmp.content = desc
            tmp.last_update = datetime.datetime.now()
            tmp.save()
            print 'update record',xid
        else:
            tmp = M_Item(title=title, content=desc, last_update=datetime.datetime.now())
            print 'add record'
            tmp.save()
        print tmp.id

        return redirect('/')

    else:
        return redirect('/')


