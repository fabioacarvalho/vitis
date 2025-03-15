from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from clients.permissions import IsCompanyUser

from clients.serializers import ClientSerializer
from clients.services import ClientService


# Views para Clients
class ClientListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicione a permissão aqui

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Termo de busca',
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: ClientSerializer(many=True)},
    )
    def get(self, request, client_id: int = None):
        if client_id:
            result = ClientService.get_client_by_id(client_id)
            serializer = ClientSerializer(result)
            return Response(serializer.data)
        result = ClientService.get_all_clients()
        serializer = ClientSerializer(result, many=True)
        return Response(serializer.data)


class ClientCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicione a permissão aqui

    @swagger_auto_schema(
        request_body=ClientSerializer,
        responses={201: ClientSerializer()},
    )
    def post(self, request):
        data = request.data
        result = ClientService.create_client(data)
        if result:
            return Response(result, status=201)
        return Response({"error": "Invalid data"}, status=400)


class ClientUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicione a permissão aqui

    @swagger_auto_schema(
        request_body=ClientSerializer,
        responses={200: ClientSerializer()},
    )
    def put(self, request, client_id):
        data = request.data
        result = ClientService.update_client(client_id, data)
        if result:
            return Response(result)
        return Response({"error": "Company not found or invalid data"}, status=404)


class ClientDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicione a permissão aqui

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, client_id):
        success = ClientService.delete_client(client_id)
        if success:
            return Response(status=204)
        return Response({"error": "Company not found"}, status=404)


# ===============  SHORT MODEL =============== #
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Client
# from .serializers import ClientSerializer
# from .permissions import IsCompanyUser

# class ClientViewSet(viewsets.ModelViewSet):
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated, IsCompanyUser]

#     def get_queryset(self):
#         # Retorna apenas os clientes da empresa do usuário logado
#         return Client.objects.filter(company=self.request.user.company)

#     def perform_create(self, serializer):
#         # Ao criar um cliente, vincula à empresa do usuário automaticamente
#         serializer.save(company=self.request.user.company)

