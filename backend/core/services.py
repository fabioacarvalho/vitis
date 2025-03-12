from .models import Company
from .serializers import CompanySerializer


class CompanyService:
    @staticmethod
    def get_all_companies():
        return Company.objects.all()

    @staticmethod
    def get_company_by_id(company_id):
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return None

    @staticmethod
    def create_company(data):
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    @staticmethod
    def update_company(company_id, data):
        company = CompanyService.get_company_by_id(company_id)
        if company:
            serializer = CompanySerializer(company, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
        return None

    @staticmethod
    def delete_company(company_id):
        company = CompanyService.get_company_by_id(company_id)
        if company:
            company.delete()
            return True
        return False