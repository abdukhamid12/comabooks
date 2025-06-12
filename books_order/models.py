from django.db import models

# Create your models here.
class SelectorRecipient(models.Model):
    get_recipient = models.CharField(max_length=150, default="GetRecip")


class Preview(models.Model):
    pass

class QuestionSelector(models.Model):
    question = models.CharField(max_length=250)


class Photo_add(models.Model):
    pass


class Testimonials(models.Model):
    comments = models.CharField(max_length=250, default="Comments")