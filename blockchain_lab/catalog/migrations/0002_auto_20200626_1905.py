# Generated by Django 3.0.3 on 2020-06-26 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='TableFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(null=True, upload_to='uploads/')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.Table')),
            ],
        ),
    ]