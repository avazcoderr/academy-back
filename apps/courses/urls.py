from django.urls import path

from apps.courses.views import (
    introduction_list,
    course_list_create_view,
    course_detail_view,
    topic_lessons_view
)

urlpatterns = [
    path("", course_list_create_view, name="course-list-create"),
    path("detail/<int:id>/", course_detail_view, name="course-detail"),
    path("introduction/", introduction_list, name="introduction-list"),

    path("topics/<int:topic_id>/lessons/", topic_lessons_view, name="topic-lessons"),
]