from rest_framework import serializers
from apps.courses.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
            'description': {'required': False}
        }
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty or whitespace.")
        return value
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
