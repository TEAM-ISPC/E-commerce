from django.urls import path, include
from .views import LoginView, LogoutView

urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

     path('auth/registro/',
         SignupView.as_view(), name='auth_signup'),

     path('user/profile/',
         ProfileView.as_view(), name='user_profile'),

     path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),

     path('agregarproducto/',
         agregarProducto.as_view(), name='agregar_producto'),
     
]