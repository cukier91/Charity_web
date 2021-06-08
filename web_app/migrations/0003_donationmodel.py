# Generated by Django 3.2.4 on 2021-06-07 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_app', '0002_institutionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('phone_no', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=20)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField(null=True)),
                ('categories', models.ManyToManyField(to='web_app.CategoryModel')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.institutionmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]