from django.db import models

# Create your models here.
class uploadfiles(models.Model):
    name=models.CharField(max_length=100)
    file=models.ImageField(upload_to='profiles/') #for image file upload
    file1=models.FileField(upload_to='files/') #for any type of file upload(pdf,docx,txt etc)
    def __str__(self):
        return self.name