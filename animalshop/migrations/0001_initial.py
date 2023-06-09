# Generated by Django 4.1.7 on 2023-03-09 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='animalshop/img/')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('выполнен', 'completed'), ('размещен', 'posted'), ('обработан', 'processed')], max_length=30)),
                ('pet_info', models.ManyToManyField(to='animalshop.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animalshop.animaltype'),
        ),
        migrations.AddField(
            model_name='animal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animalshop.category'),
        ),
        migrations.AddField(
            model_name='animal',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animalshop.status'),
        ),
    ]
