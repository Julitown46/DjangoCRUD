from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(Score, ScoreAdmin)