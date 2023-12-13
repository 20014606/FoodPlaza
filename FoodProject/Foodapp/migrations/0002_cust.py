from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('CustId', models.AutoField(primary_key=True, serialize=False)),
                ('CustName', models.CharField(max_length=30)),
                ('CustEmail', models.CharField(max_length=50)),
                ('CustPass', models.CharField(max_length=60)),
                ('CustCont', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'FP_Cust',
            },
        ),
    ]
