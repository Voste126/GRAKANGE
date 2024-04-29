##serialization of the data to be sent to the user
from rest_framework import serializers
from .models import Farmer, Farm

## serlization of farmer
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

    def create(self, validated_data):
        '''Create a new farmer with the given data
        param validated_data: The data to create the farmer with
        return: The created farmer
        '''

        Fname = validated_data.get('FName')
        Sname = validated_data.get('SurName')
        NationalID = validated_data.get('NationalID')
        Phone = validated_data.get('Phone')
        Email = validated_data.get('Email')
        County = validated_data.get('County')
        SubCounty = validated_data.get('SubCounty')
        Ward = validated_data.get('Ward')
        Location = validated_data.get('Location')
        SubLocation = validated_data.get('SubLocation')
        LandSize = validated_data.get('LandSize')
        Speciality = validated_data.get('Speciality')

        farmer = Farmer.objects.create(FName=Fname, SurName=Sname, NationalID=NationalID, Phone=Phone, Email=Email, County=County, SubCounty=SubCounty, Ward=Ward, Location=Location, SubLocation=SubLocation, LandSize=LandSize, Speciality=Speciality)
        return farmer
    
    def update(self, instance, validated_data):
        '''Update the farmer with the given data
        :param instance: The farmer to be updated
        :param validated_data: The data to update the farmer with
        :return: The updated farmer
        '''

        instance.FName = validated_data.get('FName', instance.FName)
        instance.SurName = validated_data.get('SurName', instance.SurName)
        instance.NationalID = validated_data.get('NationalID', instance.NationalID)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.County = validated_data.get('County', instance.County)
        instance.SubCounty = validated_data.get('SubCounty', instance.SubCounty)
        instance.Ward = validated_data.get('Ward', instance.Ward)
        instance.Location = validated_data.get('Location', instance.Location)
        instance.SubLocation = validated_data.get('SubLocation', instance.SubLocation)
        instance.LandSize = validated_data.get('LandSize', instance.LandSize)
        instance.Speciality = validated_data.get('Speciality', instance.Speciality)
        instance.save()
        return instance
    
## serlization of farm
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

    def create(self, validated_data):
        '''Create a new farm with the given data
        param validated_data: The data to create the farm with
        return: The created farm
        '''

        Farmer = validated_data.get('Farmer')
        FarmName = validated_data.get('FarmName')
        FarmSize = validated_data.get('FarmSize')
        FarmLocation = validated_data.get('FarmLocation')
        FarmSpeciality = validated_data.get('FarmSpeciality')

        farm = Farm.objects.create(Farmer=Farmer, FarmName=FarmName, FarmSize=FarmSize, FarmLocation=FarmLocation, FarmSpeciality=FarmSpeciality)
        return farm
    
    def update(self, instance, validated_data):
        '''Update the farm with the given data
        :param instance: The farm to be updated
        :param validated_data: The data to update the farm with
        :return: The updated farm
        '''

        instance.Farmer = validated_data.get('Farmer', instance.Farmer)
        instance.FarmName = validated_data.get('FarmName', instance.FarmName)
        instance.FarmSize = validated_data.get('FarmSize', instance.FarmSize)
        instance.FarmLocation = validated_data.get('FarmLocation', instance.FarmLocation)
        instance.FarmSpeciality = validated_data.get('FarmSpeciality', instance.FarmSpeciality)
        instance.save()
        return instance
