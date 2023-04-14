# Generated by Django 4.2 on 2023-04-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido', models.CharField(blank=True, max_length=15, null=True)),
                ('clase', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono', models.CharField(blank=True, max_length=12, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'order_with_respect_to': 'descripcion',
            },
        ),
    ]
