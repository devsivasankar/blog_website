from django.db import models
from django.contrib.auth.models import User

class Adminblog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    content = models.TextField()
    published_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Adminblog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} bookmarked {self.blog.title}"


class Comments(models.Model):
    post = models.ForeignKey(Adminblog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
