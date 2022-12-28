from django.db import models

# Create your models here.
class Question(models.Model):
    questionId = models.AutoField(primary_key=True)
    questionLabel = models.CharField(max_length=100)
    questionDataType = models.CharField(max_length=100)

