from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0004_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('CartId', models.AutoField(primary_key=True, serialize=False)),
                ('CustEmail', models.CharField(max_length=50)),
                ('FoodId', models.CharField(max_length=50)),
                ('FoodQuant', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'FP_Cart',
            },
        ),
    ]
