# Generated by Django 3.2.5 on 2022-05-18 09:32

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_bookings', to='home.hotel'),
        ),
        migrations.AlterField(
            model_name='hotelimages',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.hotel'),
        ),
    ]
