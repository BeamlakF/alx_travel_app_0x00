from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request):
        return Response({"message": "API is working!"})

urlpatterns = [
    path('test/', TestView.as_view()),
]