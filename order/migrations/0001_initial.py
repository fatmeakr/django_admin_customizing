# Generated by Django 4.0.4 on 2022-04-24 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Paied'), (2, 'Failed')], default=0, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='product.product')),
            ],
        ),
    ]
