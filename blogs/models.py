from django.db import models
 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey('home.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
