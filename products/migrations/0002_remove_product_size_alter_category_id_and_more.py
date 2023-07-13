# Generated by Django 4.1 on 2023-07-13 09:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order_one',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('1e08bc25-6d4d-444f-aa3f-786f6e10117a'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('size', models.CharField(max_length=15)),
                ('sub_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sub_category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]