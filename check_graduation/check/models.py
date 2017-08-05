from django.db import models



class Category(models.Model): # 교양43, 전공 66, 교직22, 총 140
    title = models.CharField(max_length = 20, unique = True) 
    need = models.IntegerField()

    def __str__(self):
        return self.title


class CategoryDetail(models.Model): # 전공일반, 전공핵심, 의사소통, 창의적사고 등등
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 50, unique = True)
    need = models.IntegerField()

    def __str__(self):
        return self.title

class Subject(models.Model): # 과목정보들
    category_detail = models.ForeignKey(CategoryDetail)
    title = models.CharField(max_length = 50, unique = True)
    credit = models.IntegerField()
    select = models.BooleanField()

    def __str__(self):
        return self.title