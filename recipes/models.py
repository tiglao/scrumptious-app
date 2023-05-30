from django.db import models
#from django.forms import ModelForm

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     summary = models.CharField(max_length=1000)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     is_published = models.BooleanField(default=False)

# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "summary",
#             "content",
#             "is_published",
#         ]
