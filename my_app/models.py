from django.db import models

class Todo(models.Model):
    added_date = models.DateTimeField()
    todo = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.todo)
