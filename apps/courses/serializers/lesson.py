from rest_framework import serializers
from apps.courses.models import Course, Lesson
import os


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
            video_path = obj.video.path
            hls_dir = os.path.join(os.path.dirname(video_path), 'hls')
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            m3u8_file = os.path.join(hls_dir, f"{base_name}.m3u8")
            if os.path.exists(m3u8_file):
                # m3u8 faylning media urlini qaytarish
                hls_url = os.path.join(
                    os.path.dirname(obj.video.url), 'hls', f"{base_name}.m3u8"
                )
                return request.build_absolute_uri(hls_url)
            # Agar m3u8 yo'q bo'lsa, oddiy video urlni qaytaradi
            return request.build_absolute_uri(obj.video.url)
        return None

    def get_document_url(self, obj):
        request = self.context.get('request')
        if obj.document and request:
            return request.build_absolute_uri(obj.document.url)
        return None
