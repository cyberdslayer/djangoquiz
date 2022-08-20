from django.db import models

# Create your models here.

# Creating model for qestions
class QuizName(models.Model):
    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name
    




class Question(models.Model):
    quiz = models.ForeignKey(QuizName, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null = True)
    op1 = models.CharField(max_length=200, null= True)
    op2 = models.CharField(max_length=200, null= True)
    op3 = models.CharField(max_length=200, null= True)
    op4 = models.CharField(max_length=200, null= True)
    ans = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.question
