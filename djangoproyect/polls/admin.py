# -*- coding: utf-8 -*-
# from django.contrib import admin
# from polls.models import Choice, Question
# 
# 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
# #         ('Question Information', {'fields': ['question_text']}),
# #         ('Date information',     {'fields': ['pub_date'],     'classes':['collapse']}),
#         ('Question Information', {'fields': ['question_text']}),
#         ('Date information',     {'fields': ['pub_date']}),
#     ]
# 
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)


#Ejemplo numero 2
from django.contrib import admin
from polls.models import Choice, Question
from polls.models import prueba


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class estaPrueba(admin.ModelAdmin):
    fielsets = [
                ('Esta es una prueba', {'Campo prueba':['prueba']})                
                ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ingrese pregunta',               {'fields': ['question_text']}),
        ('Informacion de la Fecha', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    #list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
