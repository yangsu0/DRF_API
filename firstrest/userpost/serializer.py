from .models import UserPost
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'
        # read_only_fields=('title',)