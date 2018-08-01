from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length= 200)
    created = models.DateTimeField("Date Loved", auto_now=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=20)
    created = models.DateTimeField("Date Created")
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text