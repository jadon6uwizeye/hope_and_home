from rest_framework import serializers
from dashboard.models import Family

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'