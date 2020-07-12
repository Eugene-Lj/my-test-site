# Generated by Django 3.0.3 on 2020-07-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.AddField(
            model_name='procurement',
            name='files',
            field=models.ManyToManyField(to='catalog.ProcurementFiles'),
        ),
    ]