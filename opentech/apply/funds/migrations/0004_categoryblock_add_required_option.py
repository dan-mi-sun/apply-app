# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 11:54
from __future__ import unicode_literals

from django.db import migrations
import opentech.apply.categories.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0003_applicationform_category_fundpageform_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='form_fields',
            field=wagtail.wagtailcore.fields.StreamField((('char', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.wagtailcore.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('text', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.wagtailcore.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('number', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.wagtailcore.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('checkbox', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('default_value', wagtail.wagtailcore.blocks.BooleanBlock(required=False))), group='Fields')), ('radios', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Choice')))), group='Fields')), ('dropdown', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Choice')))), group='Fields')), ('checkboxes', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('checkboxes', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label='Checkbox')))), group='Fields')), ('date', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.wagtailcore.blocks.DateBlock(required=False))), group='Fields')), ('time', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.wagtailcore.blocks.TimeBlock(required=False))), group='Fields')), ('datetime', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.wagtailcore.blocks.DateTimeBlock(required=False))), group='Fields')), ('image', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('file', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(label='Label')), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('text_markup', wagtail.wagtailcore.blocks.RichTextBlock(group='Other', label='Paragraph')), ('category', wagtail.wagtailcore.blocks.StructBlock((('field_label', wagtail.wagtailcore.blocks.CharBlock(help_text='Leave blank to use the default Category label', label='Label', required=False)), ('help_text', wagtail.wagtailcore.blocks.TextBlock(label='Leave blank to use the default Category help text', required=False)), ('category', opentech.apply.categories.blocks.ModelChooserBlock('categories.Category')), ('multi', wagtail.wagtailcore.blocks.BooleanBlock(label='Multi select', required=False)), ('required', wagtail.wagtailcore.blocks.BooleanBlock(label='Required', required=False))), group='Custom')))),
        ),
    ]