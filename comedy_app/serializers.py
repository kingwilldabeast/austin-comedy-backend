from rest_framework import serializers
from .models import open_mic

class OpenMicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = open_mic
        fields = ('id', 'name', 'host', 'start_time', 'link', 'ig_link', 'venue', 'address', 'weekday', 'frequency', 'image_url', 'notes')
        