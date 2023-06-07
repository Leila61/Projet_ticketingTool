from django.shortcuts import render

# Create your views here.
def communication(request):
    return render(request, 'services/communication.html')

def historique(request):
    return render(request, 'services/historiques.html')
