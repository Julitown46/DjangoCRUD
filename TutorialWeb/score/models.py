from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Name = {self.name}, Value = {self.value}"

    class Meta:
        ordering = ["name"]