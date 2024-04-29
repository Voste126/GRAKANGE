##retailers of the app serializers.py
from rest_framework import serializers
from .models import Business, Customer

## serlization of customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        '''Create a new customer with the given data
        param validated_data: The data to create the customer with
        return: The created customer
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

        customer = Customer.objects.create(FName=Fname, SurName=Sname, NationalID=NationalID, Phone=Phone, Email=Email, County=County, SubCounty=SubCounty, Ward=Ward, Location=Location, SubLocation=SubLocation, LandSize=LandSize, Speciality=Speciality)
        return customer
    
    def update(self, instance, validated_data):
        '''Update the customer with the given data
        :param instance: The customer to be updated
        :param validated_data: The data to update the customer with
        :return: The updated customer
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

## serlization of business
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

    def create(self, validated_data):
        '''Create a new business with the given data
        param validated_data: The data to create the business with
        return: The created business
        '''
        BusinessName = validated_data.get('BusinessName')
        BusinessLocation = validated_data.get('BusinessLocation')
        BusinessSpeciality = validated_data.get('BusinessSpeciality')
        BusinessSize = validated_data.get('BusinessSize')
        customer = validated_data.get('Customer')
        business = Business.objects.create(BusinessName=BusinessName, BusinessLocation=BusinessLocation, BusinessSpeciality=BusinessSpeciality, BusinessSize=BusinessSize, Customer=customer)
        return business
    
    def update(self, instance, validated_data):
        '''Update the business with the given data
        :param instance: The business to be updated
        :param validated_data: The data to update the business with
        :return: The updated business
        '''
        instance.BusinessName = validated_data.get('BusinessName', instance.BusinessName)
        instance.BusinessLocation = validated_data.get('BusinessLocation', instance.BusinessLocation)
        instance.BusinessSpeciality = validated_data.get('BusinessSpeciality', instance.BusinessSpeciality)
        instance.BusinessSize = validated_data.get('BusinessSize', instance.BusinessSize)
        instance.save()
        return instance
