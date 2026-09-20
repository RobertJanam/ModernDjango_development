from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    publisher = models.CharField(max_length=100)
    ebook = models.BooleanField(default=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Publisher: {self.publisher}, E-Book: {self.ebook}"