from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_activated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Product(models.Model):
    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('beige', 'Beige'),
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('natural', 'Natural Wood'),
        ('other', 'Other'),
    ]

    MATERIAL_CHOICES = [
        ('wood', 'Wood'),
        ('metal', 'Metal'),
        ('plastic', 'Plastic'),
        ('glass', 'Glass'),
        ('fabric', 'Fabric'),
        ('leather', 'Leather'),
        ('composite', 'Composite'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='other')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
