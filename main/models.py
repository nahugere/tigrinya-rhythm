from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=400, null=False, blank=False)
    sound = models.CharField(max_length=200, blank=True, default="", null=True)
    last_word = models.CharField(max_length=200, blank=True, default="", null=True)
    second_last_word = models.CharField(max_length=200, blank=True, default="", null=True)

    def __str__(self):
        return self.word
