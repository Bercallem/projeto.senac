from django.urls import path
from senac import views as views_senac

urlpatterns = [
    path('', views_senac.senac, name='view1'),
    path('views2/', views_senac.views2)
]
