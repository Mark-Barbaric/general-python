from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=12)

    def __str__(self):
        return self.full_name