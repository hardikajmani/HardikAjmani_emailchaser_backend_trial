# Generated by Django 4.2 on 2023-04-16 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_connectedemail_provider"),
        ("lead", "0002_remove_lead_registered_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="registered_user",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="core.user"
            ),
            preserve_default=False,
        ),
    ]
