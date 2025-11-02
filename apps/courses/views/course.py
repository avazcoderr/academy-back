from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from apps.courses.models import Course, Topic
from apps.courses.serializers import CourseSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    """
    View to list all courses or create a new course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "message": "Courses retrieved successfully",
                "result": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "Course created successfully",
                "result": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific course by ID.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        """
        Retrieve a course by ID along with its topics.
        """
        topics = Topic.objects.filter(course_id=kwargs['id']).values('id', 'title', 'content')
        instance = self.get_object()
        data = {
            "course": {
                "id": instance.id,
                "title": instance.title,
                "description": instance.description,
                "duration": instance.duration,
                "is_active": instance.is_active,
                "is_premium": instance.is_premium,
            },
            "topics": list(topics)
        }
        return Response(
            {
                "message": "Course retrieved successfully",
                "result": data
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "message": "Course deleted successfully",
                "result": None
            },
            status=status.HTTP_204_NO_CONTENT
        )


course_list_create_view = CourseListCreateView.as_view()
course_detail_view = CourseDetailView.as_view()

print(Response)
