from django.db import models


COUNTRY_CHOICES =(
    ("Brazil","Brazil"),
    ("Burundi","Burundi"),
    ("Colombia","Colombia"),
    ("Costa Rica","Costa Rica"),
    ("Dominican Republic","Dominican Republic"),
    ("Ecuador","Ecuador"),
    ("El Salvador","El Salvador"),
    ("Ethiopia","Ethiopia"),
    ("Guatemala","Guatemala"),
    ("Haiti","Haiti"),
    ("Honduras","Honduras"),
    ("India","India"),
    ("Indonesia","Indonesia"),
    ("Jamaica","Jamaica"),
    ("Kenya","Kenya"),
    ("Mexico","Mexico"),
    ("Nicaragua","Nicaragua"),
    ("Papua New Guinea","Papua New Guinea"),
    ("Peru","Peru"),
    ("Rwanda","Rwanda"),
    ("Tanzania","Tanzania"),
    ("United States","United States"),
    ("Uganda","Uganda"),
    ("Yemen","Yemen"),
    ("Zambia","Zambia"),
)

PROCESSING_CHOICES =(
    ("Washed", "Washed"),
    ("Natural", "Natural"),
    ("Black Honey", "Black Honey"),
    ("Red Honey", "Red Honey"),
    ("Yellow Honey", "Yellow Honey"),
    ("White Honey", "White Honey"),
)

RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

PREP_CHOICES = (
    ("Aeropress", "Aeropress"),
    ("Chemex", "Chemex"),
    ("French Press", "French Press"),
    ("V60", "V60"),
    ("", ""),
)

class Cup (models.Model):
    date_consumed = models.CharField(max_length=15)
    roast_date = models.CharField(max_length=15)
    country = models.CharField(
        max_length = 50,
        choices = COUNTRY_CHOICES,
        default = '1'
        )
    processing_method = models.CharField(
        max_length = 15,
        choices = PROCESSING_CHOICES,
        default = '1'
        )
    preperation_method = models.CharField(
        max_length = 15,
        choices = PREP_CHOICES,
        default = '1'
        )
    notes = models.CharField(max_length=200)
    rating = models.CharField(
        max_length = 3,
        choices = RATING_CHOICES,
        default = '1'
        )

    def __str__(self):
        return str(self.date_consumed)
