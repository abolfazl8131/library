from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import *
class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['genre']