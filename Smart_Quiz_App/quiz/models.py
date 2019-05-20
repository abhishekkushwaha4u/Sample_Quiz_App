from django.db import models


class multiple_choice(models.Model):
    question_number = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=10)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)

    def __str__(self):
           return "{}) {} \n {} \t {} \n {} \t {}".format(self.question_number, self.question, self.a, self.b, self.c, self.d)







