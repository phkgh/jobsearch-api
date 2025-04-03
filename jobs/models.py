from django.db import models


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, db_index=True)
    location = models.CharField(max_length=255, db_index=True)
    salary = models.IntegerField(db_index=True)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
