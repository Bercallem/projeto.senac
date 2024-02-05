from django.shortcuts import render

# Create your views here.

def senac (request):
    return render(
        request, 
        'senac1/index.html'
    )
    
    
def views2 (request):
    return render(
        request, 
        'senac1/main.html'
    )