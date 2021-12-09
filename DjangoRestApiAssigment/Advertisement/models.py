from django.db import models


class Advertisement(models.Model):
    """Django model for Advertisement"""

    website_url = models.URLField()

    start_date = models.DateField()
    end_date = models.DateField()

    price = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=256)
    photo_url = models.URLField()
    transaction_number = models.CharField(max_length=12)
