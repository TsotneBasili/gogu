from django.db import migrations
from django.utils.text import slugify


def add_default_categories(apps, schema_editor):
    Category = apps.get_model('catalog', 'Category')
    
    default_categories = [
        'chair',
        'sofa',
        'table',
        'wardrobe',
        'bed',
        'cabinet',
        'shelf',
        'armchair',
        'outdoor furniture',
    ]
    
    for category_name in default_categories:
        Category.objects.get_or_create(
            slug=slugify(category_name),
            defaults={
                'name': category_name.title(),
                'description': f'Browse our collection of {category_name}',
                'is_activated': True,
            }
        )


def remove_default_categories(apps, schema_editor):
    Category = apps.get_model('catalog', 'Category')
    default_slugs = [
        'chair', 'sofa', 'table', 'wardrobe', 'bed',
        'cabinet', 'shelf', 'armchair', 'outdoor-furniture'
    ]
    Category.objects.filter(slug__in=default_slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_categories, remove_default_categories),
    ]
