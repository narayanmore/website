from django.db import models

# Create your models here.
class contact(models.Model):
    from_email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=400)
    def __str__(self):
        return self.from_email
