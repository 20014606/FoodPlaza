from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0002_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust',
            name='CustCont',
            field=models.CharField(max_length=10),
        ),
    ]
