from django.shortcuts import render

from apps.courses.models import Category
from apps.courses.serializers import CategorySerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import permissions


class IntroductionListAPIView(ListAPIView):
    """
    View to list all categories without pagination.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None  # Disable pagination for this view
    permission_classes = [permissions.AllowAny]

    
    def list(self, request, *args, **kwargs):
        """
        List all categories without pagination.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "message": "List of all categories",
            "result": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
introduction_list = IntroductionListAPIView.as_view()