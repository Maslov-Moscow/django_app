from django.db import models
from djrichtextfield.models import RichTextField
from solo.models import SingletonModel


class MainPage(SingletonModel):
    title = models.CharField("Title", blank=True, max_length=100)
    bio = RichTextField("BIO")

    class Meta:
        verbose_name = "Main page"

    def __str__(self) -> str:
        return self._meta.verbose_name

    
