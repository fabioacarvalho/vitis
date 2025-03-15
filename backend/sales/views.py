from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import LeadSerializer, DealSerializer, StageSerializer, ActivitySerializer
from .services import LeadService, DealService, StageService, ActivityService
from .permissions import IsCompanyUser


class LeadListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Termo de busca',
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: LeadSerializer(many=True)},
    )
    def get(self, request):
        result = LeadService.get_leads_by_company(request.user.company)
        serializer = LeadSerializer(result, many=True)
        return Response(serializer.data)


class LeadCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=LeadSerializer,
        responses={201: LeadSerializer()},
    )
    def post(self, request):
        data = request.data
        lead = LeadService.create_lead(data)
        serializer = LeadSerializer(lead)
        return Response(serializer.data, status=201)


class LeadUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=LeadSerializer,
        responses={200: LeadSerializer()},
    )
    def put(self, request, lead_id):
        data = request.data
        lead = LeadService.update_lead(lead_id, data)
        serializer = LeadSerializer(lead)
        return Response(serializer.data)


class LeadDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, lead_id):
        success = LeadService.delete_lead(lead_id)
        if success:
            return Response(status=204)
        return Response({"error": "Lead not found"}, status=404)


# ============ Views to DEAL ============ #
class DealListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Termo de busca',
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: DealSerializer(many=True)},
    )
    def get(self, request):
        result = DealService.get_deals_by_company(request.user.company)
        serializer = DealSerializer(result, many=True)
        return Response(serializer.data)


class DealCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=DealSerializer,
        responses={201: DealSerializer()},
    )
    def post(self, request):
        data = request.data
        deal = DealService.create_deal(data)
        serializer = DealSerializer(deal)
        return Response(serializer.data, status=201)


class DealUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=DealSerializer,
        responses={200: DealSerializer()},
    )
    def put(self, request, deal_id):
        data = request.data
        deal = DealService.update_deal(deal_id, data)
        serializer = DealSerializer(deal)
        return Response(serializer.data)


class DealDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, deal_id):
        success = DealService.delete_deal(deal_id)
        if success:
            return Response(status=204)
        return Response({"error": "Deal not found"}, status=404)


# ============ Views to STAGE ============ #
class StageListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={200: StageSerializer(many=True)},
    )
    def get(self, request):
        result = StageService.get_stages_by_company(request.user.company)
        serializer = StageSerializer(result, many=True)
        return Response(serializer.data)


class StageCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=StageSerializer,
        responses={201: StageSerializer()},
    )
    def post(self, request):
        data = request.data
        stage = StageService.create_stage(data)
        serializer = StageSerializer(stage)
        return Response(serializer.data, status=201)


class StageUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=StageSerializer,
        responses={200: StageSerializer()},
    )
    def put(self, request, stage_id):
        data = request.data
        stage = StageService.update_stage(stage_id, data)
        serializer = StageSerializer(stage)
        return Response(serializer.data)


class StageDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, stage_id):
        success = StageService.delete_stage(stage_id)
        if success:
            return Response(status=204)
        return Response({"error": "Stage not found"}, status=404)



# ============ Views to Activities ============ #
class ActivityListView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={200: ActivitySerializer(many=True)},
    )
    def get(self, request):
        result = ActivityService.get_activities_by_deal(request.user.company)
        serializer = ActivitySerializer(result, many=True)
        return Response(serializer.data)


class ActivityCreateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=ActivitySerializer,
        responses={201: ActivitySerializer()},
    )
    def post(self, request):
        data = request.data
        activity = ActivityService.create_activity(data)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data, status=201)


class ActivityUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        request_body=ActivitySerializer,
        responses={200: ActivitySerializer()},
    )
    def put(self, request, activity_id):
        data = request.data
        activity = ActivityService.update_activity(activity_id, data)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)


class ActivityDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsCompanyUser]

    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, activity_id):
        success = ActivityService.delete_activity(activity_id)
        if success:
            return Response(status=204)
        return Response({"error": "Activity not found"}, status=404)
