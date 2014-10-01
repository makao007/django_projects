from django.shortcuts import render
from django.shortcuts import render_to_response

from models import tag as m_tag, category as m_category, novel as m_novel
from etc.site_info import site

def index (request):
    tags =m_tag.objects.all()
    categories = m_category.objects.all()

    info = m_novel.objects.all()
    for item in categories:
        item.novels = m_novel.objects.filter (category__id=item.id)

    return render_to_response ('index.html',{'site':site, 'tags': tags, 'categories': categories, 'novels':info})


def novel (request,xid):
    categories = m_category.objects.all()
    data = m_novel.objects.filter (id=xid)[0]

    return render_to_response ('novel.html', {'title':data.title, 'content': data.content, 'categories':categories, 'site':site})


def tag (request, xid):
    categories = m_category.objects.all()
    data = m_tag.objects.filter (id=xid)[0]
    novels = m_novel.objects.filter (tag__id=xid)
    print novels,novels
    return render_to_response ('tag.html', {'title': data.name, 'novels':novels, 'site':site, 'categories': categories})

def category (request, xid):
    categories = m_category.objects.all()
    data = m_category.objects.filter (id=xid)[0]
    novels = m_novel.objects.filter (category__id=xid)
    return render_to_response ('tag.html', {'title': data.name, 'novels':novels, 'site':site, 'categories': categories})

def name (request, my_name):
    categories = m_category.objects.all()
    novels = m_novel.objects.filter (content__contains=my_name)
    return render_to_response ('tag.html', {'title': my_name, 'novels':novels, 'site':site, 'categories': categories})
