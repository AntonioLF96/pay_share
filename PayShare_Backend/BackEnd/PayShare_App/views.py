from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from BackEnd.PayShare_App.models import User


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        # Ottieni i dati inviati dalla richiesta POST
        code = request.POST.get('code')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fiscal_code = request.POST.get('fiscal_code')
        birth_date = request.POST.get('birth_date')
        birth_place = request.POST.get('birth_place')
        residence = request.POST.get('residence')

        # Crea un nuovo oggetto User
        user = User(
            code=code,
            password=password,
            email=email,
            fiscalCode=fiscal_code,
            birthDate=birth_date,
            birthPlace=birth_place,
            residence=residence
        )

        # Salva l'oggetto User nel database
        user.save()

        # Restituisci una risposta JSON di conferma
        return JsonResponse({'message': 'User registered successfully.'})

    # Restituisci un errore se viene effettuata una richiesta diversa da POST
    return JsonResponse({'error': 'Invalid request method.'})

