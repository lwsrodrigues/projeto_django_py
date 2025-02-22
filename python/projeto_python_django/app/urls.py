from django.urls import path
from .views import home, index2, index3  # Importa as views das outras páginas

urlpatterns = [
    path('', home, name='index1'),
    path('index2/', index2, name='index2'),
    path('index3/', index3, name='index3'),
]
