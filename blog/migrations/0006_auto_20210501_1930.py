# Generated by Django 3.1.5 on 2021-05-01 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210501_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='catagories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.catagory'),
        ),
    ]
