from django.shortcuts import render

def Home(request):
    template_name = "halaman/base.html"
    context = {
        'title':'selamat datang di halaman Home',
        'umur':20,
    }

    return render(request, template_name, context)

def About(request):
    template_name = "About.html"
    context = {
        'title':'selamat datang di halaman About',
        'umur':20,
    }

    return render(request, template_name, context)