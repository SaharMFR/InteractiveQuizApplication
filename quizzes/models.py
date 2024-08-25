from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Quiz(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    creator_id = models.IntegerField()
    description = models.CharField(max_length=255)
    n_questions = models.IntegerField()
    full_mark = models.IntegerField()
    # taken_by = models.ManyToManyField(QuizzesUser)

class String(models.Model):
    text = models.TextField()

class Question(models.Model):
    description = models.TextField()
    choices = models.ManyToManyField(String)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    mark = models.IntegerField(default=1)

class QuizzesUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    taken_quizzes = models.ManyToManyField(Quiz, through='TakenQuizzes')

class TakenQuizzes(models.Model):
    user_id = models.ForeignKey(QuizzesUser, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'quiz_id')