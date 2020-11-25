# Generated by Django 3.0.8 on 2020-07-26 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0002_choicelvl2_questionlvl2'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='ChoiceLvl2',
            new_name='ChoiceHedge',
        ),
        migrations.RenameModel(
            old_name='QuestionLvl2',
            new_name='QuestionHedge',
        ),
        migrations.CreateModel(
            name='ChoiceTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fillform.QuestionTree')),
            ],
        ),
    ]