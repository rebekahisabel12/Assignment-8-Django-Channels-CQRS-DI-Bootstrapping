from rest_framework import serializers
from .models import AnalyticalMethod, Instrument, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class InstrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ("instrument_id", "manufacturer", "sample_type")


class AnalyticalMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalyticalMethod
        fields = ("method_name", "method_description",
                  "cost_per_sample", "instrument")


class UserSerializer(serializers.ModelSerializer):
    analyticalmethod = AnalyticalMethodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "analyticalmethod"]
