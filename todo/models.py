from django.db import models


PRIORITY = (
    ('none', 'None'),
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)


class Todo(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, default='none', max_length=7)
    is_done = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
