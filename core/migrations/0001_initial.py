# Generated by Django 4.1 on 2022-08-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_client_user_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Botlle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=10)),
                ('text', models.TextField(blank=True, null=True)),
                ('expired', models.BooleanField(default=False)),
                ('orders', models.ManyToManyField(blank=True, null=True, related_name='bottles', to='clients.order', verbose_name='заказы')),
            ],
        ),
        migrations.CreateModel(
            name='BottlesCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('bottle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottlescount', to='core.botlle')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottlescount', to='clients.order')),
            ],
        ),
    ]