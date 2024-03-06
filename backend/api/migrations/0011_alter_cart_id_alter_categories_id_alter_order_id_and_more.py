# Generated by Django 5.0.2 on 2024-03-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_cart_id_alter_categories_id_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
