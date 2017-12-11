from django.db import models


class HomePage(models.Model):
    """
    Home Page Layout

    """
    app_title = models.CharField(max_length=200)
    text = models.TextField()
    # app_image = None


