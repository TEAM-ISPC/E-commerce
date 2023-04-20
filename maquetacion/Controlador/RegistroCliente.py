""" 
Url = /RegistroCliente

En este controlador nos registramos con un usuario de tipo cliente, el cual vamos a necesitar ingresar nombre, apellido, email y contraseña.
El cliente ingresara sus datos, de los cuales la contraseña que ingresará no puede tener menos de 6 caracteres,
y tampoco se puede crear una cuenta con un correo que ya se ha utilizado.


Posee los siguiente métodos:
    - formularioRegistroCliente
    - mailDuplicado
    - contrasenaInvalida
    
    
Consume datos de los modulos Usuario, Cliente. 

""" 
