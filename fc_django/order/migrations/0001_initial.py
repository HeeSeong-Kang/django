# Generated by Django 3.1 on 2020-08-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('register_data', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('fcuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='사용자')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'fastcmpus_order',
            },
        ),
    ]
