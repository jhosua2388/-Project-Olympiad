from django.urls import path
from homepage import views



urlpatterns = [
    path('',views.home, name="inicio"),
    path('quienes/',views.quienes, name="quienes"),
    path('servicios/',views.servicios, name="servicios"),
    path('contacto/',views.contacto, name="contacto"),
    path('registro/',views.regristros, name="registro"),
]
