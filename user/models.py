from django.db import models


class Worker(models.Model):
    """
    A user with worker rights.

    This user must create reviews
    """
    name = models.CharField(max_length=512, null=False, blank=False, help_text='Worker user name')
    email = models.EmailField(max_length=512, null=False, blank=False, help_text='Worker user email')
    password = models.CharField(max_length=256, null=False, blank=False, help_text='Encrypt password')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'


class Business(models.Model):
    """
    A user with business rights.

    This user must create products
    """
    name = models.CharField(max_length=512, null=False, blank=False, help_text='Business user name')
    email = models.EmailField(max_length=512, null=False, blank=False, help_text='Business user email')
    password = models.CharField(max_length=256, null=False, blank=False, help_text='Encrypt password')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Business'
