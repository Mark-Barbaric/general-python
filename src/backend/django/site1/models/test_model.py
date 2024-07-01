from django.db import models


class TestModel(models.Model):
    first_name = models.CharField(max_length=8)
    last_name = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"