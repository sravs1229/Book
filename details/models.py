from django.db import models

# Create your models here.
class Book(models.Model):
    book_id=models.CharField(max_length=10)
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    year=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.book_name