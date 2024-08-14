from django.db import models


PRIORITY = (
    ('none', 'None'),
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)


class Todo(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, default='none', max_length=225, null=True, blank=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
