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

VARIETAL_CHOICES = (
    ("Blue Mountain","Blue Mountain"),
    ("Bourbon","Bourbon"),
    ("Catuai","Catuai"),
    ("Caturra","Caturra"),
    ("Ethiopia Heirloom","Ethiopia Heirloom"),
    ("Geisha","Geisha"),
    ("Java","Java"),
    ("Kona","Kona"),
    ("Mocha","Mocha"),
    ("Pachamara","Pachamara"),
    ("Sidamo","Sidamo"),
    ("SL28","SL28"),
    ("SL34","SL34"),
    ("Sulawesi","Sulawesi"),
    ("Sumatra","Sumatra"),
    ("Typica","Typica"),
    ("",""),
)

class Bean (models.Model):
    order_number= models.CharField(max_length=20, unique=True, null=False, blank=False)
    purchase_date = models.CharField(max_length=25)
    country = models.CharField(
        max_length = 50,
        choices = COUNTRY_CHOICES,
        default = '1'
        )
    varietal = models.CharField(
        max_length = 20,
        choices = VARIETAL_CHOICES,
        default = '1'
        )
    process = models.CharField(
        max_length = 15,
        choices = PROCESSING_CHOICES,
        default = '1'
        )
    growing_region = models.CharField(max_length=25)
    washing_station = models.CharField(max_length=25)
    elevation = models.CharField(max_length=25)
    notes = models.TextField()


    def __str__(self):
        return self.order_number
