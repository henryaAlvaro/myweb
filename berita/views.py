from django.shortcuts import render

# Create your views here.

def dashboard(request):
    template_name = "dashboard/base.html"
    context = {
        'title': 'halaman dashboard'
    }

    return render(request, template_name, context)
