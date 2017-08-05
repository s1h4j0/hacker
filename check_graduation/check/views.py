from django.shortcuts import render
from .models import Category, CategoryDetail, Subject


def subject_list(request):
    cate = Category.objects.all()
    catede = CategoryDetail.objects.all()
    sub = Subject.objects.all()
    return render(request, 'check/subject_list.html', {
        'category' : cate,
        'categoryDetail' : catede,
        'subject' : sub,
})

def post(request):
    pass
