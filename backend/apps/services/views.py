from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServiceSerializer
from .models import Service


# Create your views here.
class ServiceListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        services = Service.objects.all()

        # step 2
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response(
                {"message": "service not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ServiceSerializer(service)
        return Response(serializer.data)


class ServiceCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Service created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class ServiceUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response(
                {"message": "service not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ServiceSerializer(
            instance=service, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "service updated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class ServiceDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        try:
            service = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response(
                {"message": "service not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        service.delete()
        return Response(
            {
                "message": "service deleted successfully.",
            },
            status=status.HTTP_204_NO_CONTENT,
        )
