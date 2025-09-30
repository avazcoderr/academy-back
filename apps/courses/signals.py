from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.courses.models import Lesson
from apps.courses.utils import convert_to_hls_async
import os

@receiver(post_save, sender=Lesson)
def lesson_video_to_hls(sender, instance, created, **kwargs):
    if instance.video:
        video_path = instance.video.path
        hls_dir = os.path.join(os.path.dirname(video_path), 'hls')
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        m3u8_file = os.path.join(hls_dir, f"{base_name}.m3u8")
        if not os.path.exists(m3u8_file):
            convert_to_hls_async(video_path, hls_dir) 
