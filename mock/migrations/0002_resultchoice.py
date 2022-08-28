# Generated by Django 4.1 on 2022-08-26 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.choice')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mock.result')),
            ],
        ),
    ]
