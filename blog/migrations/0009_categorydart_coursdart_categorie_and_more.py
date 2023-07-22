# Generated by Django 4.2.2 on 2023-07-01 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_coursdart_options_alter_coursjava_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorydart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="coursdart",
            name="categorie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="blog.categoryjavas",
            ),
        ),
        migrations.AlterField(
            model_name="coursdart",
            name="code",
            field=models.TextField(max_length=50000),
        ),
        migrations.AlterField(
            model_name="coursdart",
            name="resultat",
            field=models.TextField(max_length=50000),
        ),
    ]
