from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.lista_vistorias, name='lista-vistorias'),
    path('form/inspetor/', views.form_inspetor, name='inspetor-create'),
    path('form/vistoria/', views.form_vistoria, name='vistoria-create'),
    path('form/registra-vistoria/<int:id>/', views.form_registra_vistoria, name='form-registra-vistoria'),
    path('reports/', views.reports, name='reports'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
