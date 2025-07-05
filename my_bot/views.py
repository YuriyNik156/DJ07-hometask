from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TelegramUser
from .serializers import TelegramUserSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        telegram_id = request.data.get('telegram_id')
        if TelegramUser.objects.filter(telegram_id=telegram_id).exists():
            return Response({'message': 'User already registered'}, status=status.HTTP_200_OK)

        serializer = TelegramUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserInfoAPIView(APIView):
    def get(self, request, telegram_id):
        try:
            user = TelegramUser.objects.get(telegram_id=telegram_id)
            serializer = TelegramUserSerializer(user)
            return Response(serializer.data)
        except TelegramUser.DoesNotExist:
            return Response({'error': 'Пользователь не зарегистрирован'}, status=404)
