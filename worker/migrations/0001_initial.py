# Generated by Django 4.2.7 on 2024-04-04 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=500)),
                ("price", models.DecimalField(decimal_places=2, max_digits=20)),
                ("link", models.URLField(max_length=2000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="flats/%Y/5%m/%d/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "flat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="images", to="worker.flat"
                    ),
                ),
            ],
        ),
    ]
