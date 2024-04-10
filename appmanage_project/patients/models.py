from django.db import models

class Patient(models.Model):
    patient_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    has_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
    
    
