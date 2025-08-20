from django.shortcuts import render

def home(request):
  context = {
    "title": "My App"
  }
  return render(request, 'home.html', context)


def about(request):
  return render(request, 'about.html')