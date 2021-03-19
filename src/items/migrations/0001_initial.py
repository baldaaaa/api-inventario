# Generated by Django 2.2.19 on 2021-03-18 11:40

from django.db import migrations, models
import django.db.models.deletion
import items.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carpeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('notas', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('cantidad_minima', models.IntegerField(default=0)),
                ('precio', models.FloatField(null=True)),
                ('notas', models.TextField(blank=True, max_length=1000, null=True)),
                ('codigo_qr', models.ImageField(blank=True, null=True, upload_to=items.models.upload_location)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Carpeta')),
                ('tags', models.ManyToManyField(to='items.Etiqueta')),
            ],
        ),
        migrations.AddField(
            model_name='carpeta',
            name='tags',
            field=models.ManyToManyField(to='items.Etiqueta'),
        ),
    ]
