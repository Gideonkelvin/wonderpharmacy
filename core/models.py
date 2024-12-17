from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = "Contact Us"
    
    def __str__(self):
        return f"{self.name} with the subject {self.subject}"

# Create your models here.
