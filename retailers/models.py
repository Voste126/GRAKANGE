from django.db import models

# Create your models here.
## Customers who register with farmers 

class Customer(models.Model):
    FName = models.CharField(max_length=100)
    SurName = models.CharField(max_length=100)
    NationalID = models.BigIntegerField(  blank=True)
    Phone = models.BigIntegerField( blank=True)
    Email = models.EmailField(blank=True)
    County = models.CharField(max_length=100, blank=True)
    SubCounty = models.CharField(max_length=100, blank=True)
    Ward = models.CharField(max_length=100, blank=True)
    Location = models.CharField(max_length=100, blank=True)
    SubLocation = models.CharField(max_length=100, blank=True)
    LandSize = models.FloatField(blank=True)
    Speciality = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'FName: {self.FName}, SurName: {self.SurName}, NationalID: {self.NationalID}, Phone: {self.Phone}, Email: {self.Email}, County: {self.County}, SubCounty: {self.SubCounty}, Ward: {self.Ward}, Location: {self.Location}, SubLocation: {self.SubLocation}, LandSize: {self.LandSize}, Speciality: {self.Speciality}'
##customers key business details
class Business(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    BusinessName = models.CharField(max_length=100)
    BusinessLocation = models.CharField(max_length=100)
    BusinessSpeciality = models.CharField(max_length=100)
    BusinessSize = models.FloatField()

    def __str__(self):
        return f'Customer: {self.Customer}, BusinessName: {self.BusinessName}, BusinessLocation: {self.BusinessLocation}, BusinessSpeciality: {self.BusinessSpeciality}, BusinessSize: {self.BusinessSize}'