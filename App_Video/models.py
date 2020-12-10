from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True)
    video_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    video_image = models.ImageField(upload_to='video_images', verbose_name="Image")
    video = EmbedVideoField(null=True)  
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date',]

    def __str__(self):
        return self.video_title

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.CharField(max_length=120)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
        
    def __str__(self):
        return self.comment

class Likes(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="liked_video")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker_user")


    def __str__(self):
        return self.user + " likes " + self.video