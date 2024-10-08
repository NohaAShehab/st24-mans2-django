# Generated by Django 5.1.1 on 2024-09-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='students/images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
