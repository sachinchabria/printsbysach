# Generated by Django 4.2.13 on 2024-08-10 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name': 'Print',
                'verbose_name_plural': 'Prints',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('SM', 'Small'), ('MD', 'Medium'), ('LG', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('width', models.DecimalField(decimal_places=1, max_digits=3)),
                ('length', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('print', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='store.print')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
                'ordering': ['print', 'size'],
            },
        ),
    ]
