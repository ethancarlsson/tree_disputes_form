# Generated by Django 3.0.8 on 2020-08-03 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fillform', '0006_choice2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question2',
            new_name='QuestionHedge',
        ),
        migrations.RenameModel(
            old_name='Choice2',
            new_name='ChoiceHedge',
        ),
        migrations.CreateModel(
            name='QuestionTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question2_text', models.CharField(max_length=200)),
                ('last_choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fillform.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fillform.QuestionTree')),
            ],
        ),
        migrations.AlterField(
            model_name='choicehedge',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fillform.QuestionTree'),
        ),
    ]