from django.http import JsonResponse

def home(request):
    """
    A simple placeholder view for the Listings app.
    This will be expanded in future milestones.
    """
    return JsonResponse({"message": "Welcome to ALX Travel Listings!"})
