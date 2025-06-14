from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SelectorRecipient(models.Model):
    get_recipient = models.CharField(max_length=150, default="GetRecip")

class QuestionText(models.Model):
    question_text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Вопрос: {self.question_text}"


class UserAnswer(models.Model):
    answer = models.TextField(verbose_name="Ответ:")
    created_at = models.DateTimeField(auto_now_add=True)

class Photo_add(models.Model):
    pass


class Testimonials(models.Model):
    comments = models.CharField(max_length=250, default="Comments")