# Generated by Django 4.1.3 on 2023-01-17 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registros",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user_name", models.CharField(max_length=30)),
                ("pet_type", models.CharField(max_length=30)),
                ("pet_name", models.CharField(max_length=30)),
                ("vaccine", models.CharField(max_length=5)),
            ],
        ),
    ]