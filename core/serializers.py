from rest_framework import serializers
from .models import Customer

# Serializers define the API representation.
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','address','professions','data_sheet')