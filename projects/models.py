from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(null=True, blank=True, default="images/%Y/%m/%d/default.jpg")  # upload_to="images/%Y/%m/%d/"
    video = models.FileField(null=True, blank=True, default="videos/%Y/%m/%d/default.mp4")

    def __str__(self):
        return self.title
