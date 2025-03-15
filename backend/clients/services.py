from clients.models import Client
from clients.serializers import ClientSerializer


class ClientService:
    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    @staticmethod
    def get_client_by_id(client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    @staticmethod
    def create_client(data):
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None

    @staticmethod
    def update_client(client_id, data):
        client = ClientService.get_client_by_id(client_id)
        if client:
            serializer = ClientSerializer(client, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return serializer.data
        return None

    @staticmethod
    def delete_client(client_id):
        client = ClientService.get_client_by_id(client_id)
        if client:
            client.delete()
            return True
        return False
