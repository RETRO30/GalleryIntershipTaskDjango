from django.db import models

# Create your models here.
class Image(models.Model):
    image_base64 = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=bool)

    def __str__(self):
        return f"Image(id={self.pk}, description={self.description})"