from rest_framework import serializers

from .models import Cryptocurrency

class CryptoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ('id',
                    'rank',
                    'symbol',
                    'name',
                    'supply',
                    'marketCapUsd',
                    'volumeUsd24Hr',
                    'priceUsd',
                    'changePercent24Hr',
                    'vwap24Hr')