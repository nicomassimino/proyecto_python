from django.shortcuts import render

# Create your views here.
def index(request):
    context =  {"mensaje": "Bienvenidos"}
    return render(request, "myapp/index.html", context)