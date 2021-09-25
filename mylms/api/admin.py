from django.contrib import admin
from .models import studentModel,singerModel, songModel
# Register your models here.

@admin.register(studentModel)
class studentAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in studentModel._meta.get_fields()]
    filter = ['id']
    search_fields = ['lastName','email']

@admin.register(singerModel)
class singerAdmin(admin.ModelAdmin):
    # list_display = [f.name for f in singerModel._meta.get_fields()]
    list_display = ['id','firstName','lastName','gender','created']
    filter =['firstName','gender']
    search_fields = ['firstName','gender']

@admin.register(songModel)
class songAdmin(admin.ModelAdmin):
    list_display = [f.name for f in songModel._meta.get_fields()]
    filter = ['title','singer']
    search_fields = ['singer','title']
