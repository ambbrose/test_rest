from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HeroView(APIView):
    def get(self, request):
        return Response({'msg': 'this is a success'}, status=status.HTTP_200_OK)
