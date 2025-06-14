from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    question_text = QuestionText.objects.order_by('-created_at').first()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # или на следующую страницу
    else:
        form = AnswerForm()  # обязательно создаём form при GET-запросе

    return render(request, "index.html", {
        'form': form,
        'question_text': question_text
    })