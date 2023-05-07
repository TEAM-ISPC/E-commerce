import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ItemTiendaComponent } from './component/item-tienda/item-tienda.component';
import { LoginComponent } from './component/login/login.component';
import { CarritoComponent } from './component/carrito/carrito.component';//Esto Agregué yo Lucas


const routes: Routes = [
  { path:'item', component:ItemTiendaComponent },
  { path:'login', component:LoginComponent },
  { path:'carrito', component:CarritoComponent },//Esto Agregué yo Lucas
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
