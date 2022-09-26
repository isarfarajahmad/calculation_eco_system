from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('metric1', views.metric1, name='metric1'),
    path('metric2', views.metric2, name='metric2'),
    path('metric5', views.metric5, name='metric5'),
    path('metric4', views.metric4, name='metric4'),
    path('metric3', views.metric3, name='metric3'),
    path('metric6', views.metric6, name='metric6'),
    path('metric7', views.metric7, name='metric7'),
    path('metric8', views.metric8, name='metric8'),
    path('metric9', views.metric9, name='metric9'),
    path('metric10', views.metric10, name='metric10'),
    path('metric11', views.metric11, name='metric11'),
    path('metric12', views.metric12, name='metric12'),
    path('metric13', views.metric13, name='metric13'),
    path('metric14', views.metric14, name='metric14'),
    path('metric15', views.metric15, name='metric15'),
    path('metric16', views.metric16, name='metric16'),
    path('metric17', views.metric17, name='metric17'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('report/<str:pk>/', views.report, name='report'),
    path('submission', views.submission, name='submission'),
]
