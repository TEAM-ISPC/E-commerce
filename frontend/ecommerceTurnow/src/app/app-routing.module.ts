import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ItemTiendaComponent } from './component/item-tienda/item-tienda.component';
import { LoginComponent } from './component/login/login.component';

const routes: Routes = [
  { path:'item', component:ItemTiendaComponent },
  { path:'login', component:LoginComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
