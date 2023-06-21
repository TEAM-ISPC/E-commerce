from django import urls
from django.urls import path, include, re_path
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios, agregarProducto, verProductos, verCategorias, verProductoDetalle, verCategoriaDetalle, customjsonybajarstock, retornarPagado, CarritoComprasVista


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
     
     path('retornarPagado/',
         retornarPagado.as_view(), name='retornarPagado'),
     
     path('actualizarstock/<int:pk>/<int:cantidad>', customjsonybajarstock.as_view(), name='customjsonybajarstock'),
     
    path('carrito/',
        CarritoComprasVista.as_view(), name='carritodecompras'),
     
]