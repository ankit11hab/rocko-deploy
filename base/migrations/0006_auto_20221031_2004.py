# Generated by Django 3.2.9 on 2022-10-31 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20221031_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.team'),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=124, null=True),
        ),
    ]
