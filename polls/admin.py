from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'created']
    search_fields = ['question_text']
    list_filter = ['created']
    fields = ['question_text'] #ke ke dekhaune bhanera rakhne ho
    inlines = [ChoiceInLine]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)