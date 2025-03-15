# marketing/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import CampaignSerializer
from .services import MarketingService
from core.permissions import IsCompanyUser  # Permissão personalizada para verificar o usuário da empresa

# Views para Campanhas

class CampaignListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicionando a permissão aqui

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Termo de busca para filtrar campanhas',
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: CampaignSerializer(many=True)},
    )
    def get(self, request):
        """
        Lista todas as campanhas ou pesquisa por uma campanha específica.
        """
        campaigns = Campaign.objects.all()  # Pode ser filtrado com base em parâmetros de pesquisa
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)


class CampaignCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicionando a permissão aqui

    @swagger_auto_schema(
        request_body=CampaignSerializer,
        responses={201: CampaignSerializer()},
    )
    def post(self, request):
        """
        Cria uma nova campanha.
        """
        data = request.data
        campaign = MarketingService.create_campaign(data)
        if campaign:
            return Response(CampaignSerializer(campaign).data, status=201)
        return Response({"error": "Invalid data"}, status=400)


class CampaignUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicionando a permissão aqui

    @swagger_auto_schema(
        request_body=CampaignSerializer,
        responses={200: CampaignSerializer()},
    )
    def put(self, request, campaign_id):
        """
        Atualiza uma campanha existente.
        """
        data = request.data
        campaign = MarketingService.update_campaign(campaign_id, data)
        if campaign:
            return Response(CampaignSerializer(campaign).data)
        return Response({"error": "Campaign not found or invalid data"}, status=404)


class CampaignDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]  # Adicionando a permissão aqui

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, campaign_id):
        """
        Deleta uma campanha.
        """
        success = MarketingService.delete_campaign(campaign_id)
        if success:
            return Response(status=204)
        return Response({"error": "Campaign not found"}, status=404)
