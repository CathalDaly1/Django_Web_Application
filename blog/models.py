from django.db import models


# Posts for the blog
class Post(models.Model):
    # Define cols in table
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


