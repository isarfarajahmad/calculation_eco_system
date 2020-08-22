from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('percentage', views.percentage, name='percentage'),
    path('average', views.average, name='average'),
    path('square_root', views.square_root, name='square_root'),
    path('simple_interest', views.simple_interest, name='simple_interest'),
    path('quadratic_equation', views.quadratic_equation, name='quadratic_equation'),
]
