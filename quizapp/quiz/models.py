from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)
    question_number = models.IntegerField(primary_key=True)
    
    def __str__(self):
           return "{}) {}".format(self.question_number, self.question)


class Improved_Questions(models.Model):
    question_number = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    def __str__(self):
           return "{}) {}".format(self.question_number, self.question)


