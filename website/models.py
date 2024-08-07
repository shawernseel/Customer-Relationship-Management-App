from django.db import models

# Django abstracts database requests

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #django will auto timestamp; good to have
    first_name = models.CharFeild(max_length=50)
    last_name = models.CharFeild(max_length=50)
    email = models.CharFeild(max_length=100)
    phone = models.CharFeild(max_length=15)
    address = models.CharFeild(max_length=100)
    city = models.CharFeild(max_length=50)
    state = models.CharFeild(max_length=50)
    zipcode = models.CharFeild(max_length=50)



