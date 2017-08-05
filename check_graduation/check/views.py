from django.shortcuts import render
from .models import Category, CategoryDetail, Subject


def subject_list(request):
    cate = Category.objects.all()
    catede = CategoryDetail.objects.all()
    sub = Subject.objects.all()
    count = 0
    for i in catede:
        count += i.need
    return render(request, 'check/subject_list.html', {
        'category' : cate,
        'categoryDetail' : catede,
        'subject' : sub,
        'count' : count,
})

