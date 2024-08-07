from django.db import models

# Django abstracts database requests
# Django will auto make this into a database model, no sql needed!

class Record(models.Model): #django will auto pluralise Record
    created_at = models.DateTimeField(auto_now_add=True) #django will auto timestamp; good to have
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    #if you call record on admin or webpage it will return first and last name
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

