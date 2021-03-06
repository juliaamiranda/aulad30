# Generated by Django 2.2.5 on 2019-09-27 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('senha', models.CharField(max_length=16, verbose_name='Senha')),
            ],
        ),
        migrations.AddField(
            model_name='coach',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Usuario'),
        ),
    ]
