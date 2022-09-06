# Generated by Django 4.1 on 2022-09-06 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.CharField(max_length=100)),
                ('father_alive', models.BooleanField(default=True)),
                ('father_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('father_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('father_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_occupation_other', models.CharField(blank=True, max_length=100, null=True)),
                ('mother', models.CharField(max_length=100)),
                ('mother_alive', models.BooleanField(default=True)),
                ('mother_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('mother_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mother_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_occupation_other', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=100)),
                ('dependent_children', models.IntegerField()),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Family',
                'verbose_name_plural': 'Families',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('about', models.TextField(blank=True, null=True)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.family')),
            ],
            options={
                'verbose_name': 'Child',
                'verbose_name_plural': 'Children',
            },
        ),
    ]