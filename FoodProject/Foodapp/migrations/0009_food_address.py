
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foodapp', '0008_auto_20200218_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Address',
            field=models.CharField(default='', max_length=150),
        ),
    ]
