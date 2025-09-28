from rest_framework import serializers
from apps.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "is_active",
            "is_premium"
        ]
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive integer.")
        return value