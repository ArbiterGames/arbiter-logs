from rest_framework import serializers
from logs.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    created_on = serializers.Field(source='get_utc_created_on')

    class Meta:
        model = Entry
        fields = ('data', 'created_on')
