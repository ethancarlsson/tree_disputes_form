# Generated by Django 3.0.8 on 2020-08-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0007_auto_20200803_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicetree',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionhedge',
            name='last_choices',
        ),
        migrations.RemoveField(
            model_name='questiontree',
            name='last_choices',
        ),
        migrations.DeleteModel(
            name='ChoiceHedge',
        ),
        migrations.DeleteModel(
            name='ChoiceTree',
        ),
        migrations.DeleteModel(
            name='QuestionHedge',
        ),
        migrations.DeleteModel(
            name='QuestionTree',
        ),
    ]