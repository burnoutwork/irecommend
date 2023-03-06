from django.db import models


class City(models.Model):
    """ Model with cities where goods will be placed """
    name = models.CharField(max_length=512, null=False, blank=False, help_text='City name')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Category(models.Model):
    """ Model with category of product """
    name = models.CharField(max_length=512, null=False, blank=False, help_text='Category name')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """
    Product to be reviewed.

    It can only be created by a business usere
    """
    title = models.CharField(max_length=1024, null=False, blank=False, help_text='Title of product')

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False, help_text='City')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, help_text='Category')
    creator = models.ForeignKey('user.Business', on_delete=models.CASCADE, null=False, blank=False, help_text='Creator')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Review(models.Model):
    """
    Product Reviews.

    It can only be created by a worker user
    """
    title = models.CharField(max_length=1024, null=False, blank=False, help_text='Title of review')
    description = models.TextField(max_length=2048, null=False, blank=False, help_text='Description')
    date_create = models.DateTimeField(auto_created=True, null=False, blank=False, help_text="Date create review")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, help_text='Product')
    creator = models.ForeignKey('user.Worker', on_delete=models.CASCADE, null=False, blank=False, help_text='Worker')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
