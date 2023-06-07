import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pdb

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import models
from .models import User
from rest_framework.views import APIView

class RegisterUserApiView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        code = request.data["code"]
        password = request.data["password"]
        email = request.data["email"]
        fiscal_code = request.data["fiscalCode"]
        birth_date = request.data["birthDate"]
        birth_place = request.data["birthPlace"]
        residence = request.data["residence"]
        smartContractList = request.data["smartContractList"]
        extensions = request.data["extensions"]

        user = User(
            code=code,
            password=password,
            email=email,
            fiscalCode=fiscal_code,
            birthDate=birth_date,
            birthPlace=birth_place,
            residence=residence,
            smartContractList=smartContractList,
            extensions=extensions
        )
        print(user)
        # Salva l'oggetto User nel database
        user.save()

        return Response({'message': 'User registered successfully.'}, status=status.HTTP_200_OK)


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        # Ottieni i dati inviati dalla richiesta POST
        code = request.POST.get("code")
        password = request.POST.get("password")
        email = request.POST.get("email")
        fiscal_code = request.POST.get("fiscal_code")
        birth_date = request.POST.get("birth_date")
        birth_place = request.POST.get("birth_place")
        residence = request.POST.get("residence")
        smartContractList = request.POST.get("smartContractList")
        extensions = request.POST.get("extensions")

        # Crea un nuovo oggetto User
        user = User(
            code=code,
            password=password,
            email=email,
            fiscalCode=fiscal_code,
            birthDate=birth_date,
            birthPlace=birth_place,
            residence=residence,
            smartContractList=smartContractList,
            extensions=extensions
        )

        # Salva l'oggetto User nel database
        user.save()

        # Restituisci una risposta JSON di conferma
        return JsonResponse({'message': 'User registered successfully.'})

    # Restituisci un errore se viene effettuata una richiesta diversa da POST
    return JsonResponse({'error': 'Invalid request method.'})

