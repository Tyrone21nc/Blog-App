from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField()   # my addition
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class PostImage(models.Model):
#     # this will allow users to add more than one image from their computer to their blog post
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return f"Image for {self.post.title}"

# class PostComment(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='comment')
    
