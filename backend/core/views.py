from rest_framework import generics, viewsets
from .models import Company
from .serializers import CompanySerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import CompanyService
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Views para Company
class CompanyListView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Termo de busca',
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: CompanySerializer(many=True)},
    )
    def get(self, request):
        companies = CompanyService.get_all_companies()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

class CompanyCreateView(APIView):
    @swagger_auto_schema(
        request_body=CompanySerializer,
        responses={201: CompanySerializer()},
    )
    def post(self, request):
        data = request.data
        result = CompanyService.create_company(data)
        if result:
            return Response(result, status=201)
        return Response({"error": "Invalid data"}, status=400)

class CompanyUpdateView(APIView):
    @swagger_auto_schema(
        request_body=CompanySerializer,
        responses={200: CompanySerializer()},
    )
    def put(self, request, company_id):
        data = request.data
        result = CompanyService.update_company(company_id, data)
        if result:
            return Response(result)
        return Response({"error": "Company not found or invalid data"}, status=404)

class CompanyDeleteView(APIView):
    @swagger_auto_schema(
        responses={204: "No Content"},
    )
    def delete(self, request, company_id):
        success = CompanyService.delete_company(company_id)
        if success:
            return Response(status=204)
        return Response({"error": "Company not found"}, status=404)

# Views generics for company replaced by APIView and using CompanyService
# class CompanyListView(generics.ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyCreateView(generics.CreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyUpdateView(generics.UpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class CompanyDeleteView(generics.DestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# ViewSets (opcional, para simplificar)
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

