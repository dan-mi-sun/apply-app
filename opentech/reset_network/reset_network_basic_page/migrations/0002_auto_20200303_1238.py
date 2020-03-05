# Generated by Django 2.2.9 on 2020-03-03 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_customimage_drupal_id'),
        ('reset_network_basic_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetnetworkbasicpage',
            name='social_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
        migrations.AddField(
            model_name='resetnetworkbasicpage',
            name='social_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
