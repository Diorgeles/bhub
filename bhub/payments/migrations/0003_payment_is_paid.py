# Generated by Django 5.0 on 2023-12-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_remove_payment_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="is_paid",
            field=models.BooleanField(default=False, verbose_name="Pago"),
        ),
    ]
