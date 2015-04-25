from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
