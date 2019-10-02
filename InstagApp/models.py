from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class InstagUser(AbstractUser):
    profile_img = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )


class Post(models.Model):
    author = models.ForeignKey(
        InstagUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("posts")

    def get_like_count(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        InstagUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return 'Likes: ' + self.user.username + ' likes ' + self.post.title
