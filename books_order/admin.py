from django.contrib import admin
from .models import *

admin.site.register(SelectorRecipient)
admin.site.register(Testimonials)
admin.site.register(QuestionText)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'created_at')