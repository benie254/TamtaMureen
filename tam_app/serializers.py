from rest_framework import serializers
from tam_app.models import Quote 


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote 
        fields = ('id','quote','author','source')