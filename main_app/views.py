from django.shortcuts import render

# Create your views here.
def home(request):
  
  context = {
    "title": "My App"
  }

  return render(request, 'home.html', context)