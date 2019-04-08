from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)
    question_number = models.IntegerField(primary_key=True)
    
    def __str__(self):
           return "{}) {}".format(self.question_number, self.question)

