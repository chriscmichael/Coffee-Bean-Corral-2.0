# Generated by Django 4.1.1 on 2022-09-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cup",
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
                ("date_consumed", models.CharField(max_length=15)),
                ("roast_date", models.CharField(max_length=15)),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("Brazil", "Brazil"),
                            ("Burundi", "Burundi"),
                            ("Colombia", "Colombia"),
                            ("Costa Rica", "Costa Rica"),
                            ("Dominican Republic", "Dominican Republic"),
                            ("Ecuador", "Ecuador"),
                            ("El Salvador", "El Salvador"),
                            ("Ethiopia", "Ethiopia"),
                            ("Guatemala", "Guatemala"),
                            ("Haiti", "Haiti"),
                            ("Honduras", "Honduras"),
                            ("India", "India"),
                            ("Indonesia", "Indonesia"),
                            ("Jamaica", "Jamaica"),
                            ("Kenya", "Kenya"),
                            ("Mexico", "Mexico"),
                            ("Nicaragua", "Nicaragua"),
                            ("Papua New Guinea", "Papua New Guinea"),
                            ("Peru", "Peru"),
                            ("Rwanda", "Rwanda"),
                            ("Tanzania", "Tanzania"),
                            ("United States", "United States"),
                            ("Uganda", "Uganda"),
                            ("Yemen", "Yemen"),
                            ("Zambia", "Zambia"),
                        ],
                        default="1",
                        max_length=50,
                    ),
                ),
                (
                    "process",
                    models.CharField(
                        choices=[
                            ("Washed", "Washed"),
                            ("Natural", "Natural"),
                            ("Black Honey", "Black Honey"),
                            ("Red Honey", "Red Honey"),
                            ("Yellow Honey", "Yellow Honey"),
                            ("White Honey", "White Honey"),
                        ],
                        default="1",
                        max_length=15,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        default="1",
                        max_length=3,
                    ),
                ),
            ],
        ),
    ]
