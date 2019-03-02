from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        to się musi tak nazywać .
        miejsce gdzie ma zostac przekierowany user po
        wcisnieciu Submit button w tamplate
        :return:
        """
        return reverse('blog_app:post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    # related names jest tym czym się w template odwolujemy do tego
    # i wyrzej w metodzie approve_comments po self.comments.
    post = models.ForeignKey('blog_app.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
