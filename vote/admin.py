from django.contrib import admin

from .models import Question, Choice, Room

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Room)
