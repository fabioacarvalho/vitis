from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.utils.crypto import get_random_string
from .models import CompanyInvitation, CompanyUser
from .serializers import CompanyInvitationSerializer, CompanyUserSerializer, SignInSerializer
from rest_framework.permissions import IsAuthenticated


def generate_invitation_token(length=32):
    """Gera um token seguro para convites"""
    return get_random_string(
        length=length,
        allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )


class CompanyUserViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyUserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CompanyUser.objects.filter(company=self.request.user.company)
    
    def perform_create(self, serializer):
        if not self.request.user.is_company_admin:
            raise PermissionDenied("Apenas administradores podem criar usuários")
        serializer.save(company=self.request.user.company)


class CompanyInvitationViewSet(viewsets.ModelViewSet):
    queryset = CompanyInvitation.objects.all()
    serializer_class = CompanyInvitationSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        if not self.request.user.is_company_admin:
            raise PermissionDenied("Apenas administradores podem convidar usuários")
        
        serializer.save(
            company=self.request.user.company,
            created_by=self.request.user,
            token=generate_invitation_token()
        )


class SignInView(APIView):
    """
    API View para login de usuário com autenticação usando JWT
    """
    @swagger_auto_schema(
        request_body=SignInSerializer,
        responses={200: SignInSerializer()},
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Autenticar o usuário
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Gerar o token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Preparar os dados para a resposta
        data = {
            "token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                # Adicione qualquer outro dado do usuário que queira enviar
            }
        }

        return Response(data, status=status.HTTP_200_OK)


class SignUpView(APIView):
    """
    API View para cadastro de usuário com autenticação usando JWT
    """
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Validando os dados de entrada
        if not username or not password or not email:
            return Response({"detail": "Username, email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se o username já existe
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        
        # Verifica se o email já existe
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")

        # Criando o usuário
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Gerar o token para o novo usuário
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Preparar os dados para a resposta
            data = {
                "token": access_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            }

            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"detail": f"Error creating user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    """
    API View para listar todos os usuários ou obter um usuário específico por ID.
    """

    def get(self, request, user_id=None):
        # Se o user_id for fornecido, busca um usuário específico
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
                return Response(data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Se não for fornecido um user_id, retorna todos os usuários
            users = User.objects.all()
            data = [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
                for user in users
            ]
            return Response(data, status=status.HTTP_200_OK)