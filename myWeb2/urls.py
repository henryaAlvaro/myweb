
from django.contrib import admin
from django.urls import path, include

from myWeb2.views import Home, About
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Home, name = "Home"),
    path('dashboard/', include("berita.urls"))

]
