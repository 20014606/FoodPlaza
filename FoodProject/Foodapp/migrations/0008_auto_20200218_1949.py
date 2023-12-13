from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0007_food_foodimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cust',
            old_name='CustName',
            new_name='CustFName',
        ),
        migrations.AddField(
            model_name='cust',
            name='CustLName',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
