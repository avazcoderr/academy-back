from django.urls import path

from apps.courses.views import (
    introduction_list,
    course_list_create_view,
    course_detail_view
)

urlpatterns = [
    path("", course_list_create_view, name="course-list-create"),
    path("introduction/", introduction_list, name="introduction-list"),
    path("courses/<int:id>/", course_detail_view, name="course-detail"),
]