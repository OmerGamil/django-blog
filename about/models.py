from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Represents the 'About' section content of the site.

    Fields:
        title (str): The title or heading for the About section.
        updated_on (datetime): Timestamp of the last update to the content.
        profile_image (CloudinaryField): Optional profile image to display.
        content (str): Main body of text for the About page.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Represents a request for collaboration submitted via a contact form.

    Fields:
        name (str): The name of the person submitting the request.
        email (str): The email address of the requester.
        message (str): The actual message or request content.
        read (bool): Whether the request has been marked as read by the site owner.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"