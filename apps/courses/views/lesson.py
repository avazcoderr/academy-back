from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from apps.courses.models import Lesson, Topic
from apps.courses.serializers import LessonSerializer


class TopicLessonsView(generics.ListAPIView):
    """
    View to list all lessons under a specific topic.
    """
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        topic_id = self.kwargs.get("topic_id")
        return Lesson.objects.filter(topic_id=topic_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        return Response(
            {
                "message": "Lessons retrieved successfully",
                "result": serializer.data
            },
            status=status.HTTP_200_OK
        )

topic_lessons_view = TopicLessonsView.as_view()