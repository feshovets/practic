from django.shortcuts import render

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementAPIView(APIView):
    """
        APIView class for "GET" and "POST" methods
        from url /api/container/
    """
    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Advertisement successfully created",
                             "Advertisement": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementDetails(APIView):
    """
        APIView class for "PUT", "GET" and "DELETE" requests
        from url /api/container/< id >
    """
    def get_object(self, indent):
        try:
            return Advertisement.objects.get(id=indent)
        except Advertisement.DoesNotExist:
            return Response({"status": 404, "message": "Advertisement not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, indent):
        """
        "GET" HTTP-request, obtain certificate by id
        """
        advertisement = self.get_object(indent)
        if isinstance(advertisement, Response):
            return advertisement

        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)

    def put(self, request, indent):
        """
        "PUT" HTTP-request, edit the existing record (by id)
        """
        advertisement = self.get_object(indent)
        if isinstance(advertisement, Response):
            return advertisement
        advertisement_data = JSONParser().parse(request)
        serializer = AdvertisementSerializer(advertisement, data=advertisement_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Advertisement successfully updated",
                             "Advertisement": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": 400, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, indent):
        """
        "DELETE" HTTP-request, delete certificate by id
        """
        advertisement = self.get_object(indent)
        if isinstance(advertisement, Response):
            return advertisement
        advertisement.delete()
        return Response({"status": 200, "message": "Successfully deleted!"}, status=status.HTTP_200_OK)
