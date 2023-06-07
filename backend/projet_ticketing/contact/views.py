from django.shortcuts import render

# Create your views here.
def connexion(request):
    return render(request, 'contact/connexion.html')

def inscription(request):
    return render(request, 'contact/inscription.html')