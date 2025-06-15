from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    Represents a blog post written by a user.

    Fields:
        title (str): The title of the post.
        slug (str): URL-friendly version of the title.
        author (User): ForeignKey to the User who wrote the post.
        featured_image (CloudinaryField): Optional image for the post.
        content (str): The full content of the post.
        created_on (datetime): Timestamp when the post was created.
        status (int): Indicates if post is a draft (0) or published (1).
        excerpt (str): Optional summary of the post.
        updated_on (datetime): Timestamp of the last update.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Represents a comment made by a user on a blog post.

    Fields:
        post (Post): ForeignKey linking to the related blog post.
        author (User): ForeignKey to the user who made the comment.
        body (str): The text content of the comment.
        approved (bool): Indicates if the comment has been approved by a moderator.
        created_on (datetime): Timestamp when the comment was created.
    """
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
