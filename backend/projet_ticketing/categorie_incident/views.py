from django.shortcuts import render

# Create your views here.
def moinurgent(request):
    return render(request, 'categorie_incident/moinurgent.html')

def urgent(request):
    return render(request, 'categorie_incident/urgent.html')

