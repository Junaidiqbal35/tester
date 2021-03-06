# Generated by Django 3.1 on 2020-08-09 09:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=250)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(default='Punjab', max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('additional_information', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
        ),
    ]
