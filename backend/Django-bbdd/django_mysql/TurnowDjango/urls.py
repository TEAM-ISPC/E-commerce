from django.urls import path, include
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios, agregarProducto, verProductos, verCategorias, verProductoDetalle, verCategoriaDetalle


urlpatterns = [
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
    
     path('productos/',
         verProductos.as_view(), name='ver_productos'),
     
     path('productos/<int:pk>',
         verProductoDetalle.as_view(), name='ver_productosDetalle'),
     
     path('categorias/',
         verCategorias.as_view(), name='ver_categorias'),
     
     path('categorias/<int:pk>',
         verCategoriaDetalle.as_view(), name='ver_categoriasDetalle'),

     path('agregarproducto/',
         agregarProducto.as_view(), name='agregar_producto'),
     
]