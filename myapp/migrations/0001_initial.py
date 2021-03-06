# Generated by Django 3.0.6 on 2020-10-05 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='extenduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firname', models.TextField(max_length=15)),
                ('fname', models.TextField(max_length=15)),
                ('gnpan', models.TextField(max_length=20)),
                ('gramp', models.TextField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='euser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='complaindata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
                ('gram_nagar', models.CharField(max_length=30)),
                ('com_subject', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(default='Recieved', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
