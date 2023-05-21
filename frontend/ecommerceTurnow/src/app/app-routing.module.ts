import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ItemTiendaComponent } from './component/item-tienda/item-tienda.component';
import { LoginComponent } from './component/login/login.component';
import { CarritoComponent } from './component/carrito/carrito.component';//Esto Agregué yo Lucas
import { ContactoComponent } from './component/contacto/contacto.component';
import { NosotrosComponent } from './component/nosotros/nosotros.component';


const routes: Routes = [
  { path:'item/:id', component:ItemTiendaComponent },
  { path:'login', component:LoginComponent },
  { path:'carrito', component:CarritoComponent },//Esto Agregué yo Lucas
  { path:'contacto', component:ContactoComponent},
  { path:'nosotros', component:NosotrosComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
