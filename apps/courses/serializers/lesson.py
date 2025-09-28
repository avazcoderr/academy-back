from rest_framework import serializers
from apps.courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    topic_title = serializers.CharField(source='topic.title', read_only=True)
    video_url = serializers.SerializerMethodField()
    document_url = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = [
            "id",
            "topic_title",
            "title",
            "content",
            "video_url",
            "document_url"
        ]
        read_only_fields = ["id", "topic_title", "video_url", "document_url"]
    
    def get_video_url(self, obj):
        request = self.context.get('request')
        if obj.video and request:
            return request.build_absolute_uri(obj.video.url)
        return None

    def get_document_url(self, obj):
        request = self.context.get('request')
        if obj.document and request:
            return request.build_absolute_uri(obj.document.url)
        return None
