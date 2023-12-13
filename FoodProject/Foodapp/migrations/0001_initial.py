from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('FoodId', models.AutoField(primary_key=True, serialize=False)),
                ('FoodName', models.CharField(max_length=30)),
                ('FoodCat', models.CharField(max_length=30)),
                ('FoodPrice', models.FloatField(max_length=15)),
            ],
            options={
                'db_table': 'FP_Food',
            },
        ),
    ]
