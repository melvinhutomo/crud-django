from django.db import models

# Create your models here.
class Product(models.Model):
    NOVEL = 1
    DOCUMENTATION = 2
    OTHER = 3
    BOOK_TYPES= (
        (NOVEL, 'Novel'),
        (DOCUMENTATION, 'Documentation'),
        (OTHER, 'Other'),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField(null=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    def __str__(self):
        return self.title
