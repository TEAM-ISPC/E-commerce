import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TiendaComponent } from './component/tienda/tienda.component';
import { ItemTiendaComponent } from './component/item-tienda/item-tienda.component';
import { HeaderComponent } from './component/header/header.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FooterComponent } from './component/footer/footer.component';
import { LoginComponent } from './component/login/login.component';
import { CarritoComponent } from './component/carrito/carrito.component';
import { RouterModule, Routes } from '@angular/router';


const appRoutes: Routes = [
  { path:'', component:TiendaComponent },
  { path:'item', component:ItemTiendaComponent },
  { path:'login', component:LoginComponent },
  { path:'carrito', component:CarritoComponent },
  
];

@NgModule({
  declarations: [
    AppComponent,
    TiendaComponent,
    ItemTiendaComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    CarritoComponent
     ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
