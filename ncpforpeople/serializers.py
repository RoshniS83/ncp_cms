from rest_framework import serializers
from ncpforpeople.models import People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


