from django.db import models

# Create your models here.
#models collect basic credetial for farmers that will be used as authetication and 
#authorization to the system. Collection of specifics will also be done based on abstact base classs

class Farmer(models.Model):
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

#Farm model will be used to collect specific details of the 
#farm that the farmer owns
class Farm(models.Model):
    Farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    FarmName = models.CharField(max_length=100)
    FarmSize = models.FloatField()
    FarmLocation = models.CharField(max_length=100)
    FarmSpeciality = models.CharField(max_length=100)

    def __str__(self):
        return f'Farmer: {self.Farmer}, FarmName: {self.FarmName}, FarmSize: {self.FarmSize}, FarmLocation: {self.FarmLocation}, FarmSpeciality: {self.FarmSpeciality}'




