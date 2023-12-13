from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('CustEmail', models.CharField(max_length=30)),
                ('OrderDate', models.CharField(max_length=40)),
                ('TotalBill', models.FloatField(max_length=50)),
            ],
            options={
                'db_table': 'FP_Order',
            },
        ),
    ]
