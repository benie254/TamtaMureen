from rest_framework import serializers
from tam.models import Quote 


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote 
        fields = ('id','quote','author','source')