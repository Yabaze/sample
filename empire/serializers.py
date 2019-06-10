from rest_framework import serializers
from .models import ShopDetails , FeedBackDetails , UserLogin


class ShopDetailserializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDetails
        fields = '__all__'

class FeedBackDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackDetails
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'        