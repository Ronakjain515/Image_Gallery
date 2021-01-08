from django.db import models

# Create your models here.


class ImagePost(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    imagePostId = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Images(models.Model):
    imagePostId = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")


