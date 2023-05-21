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
import { ContactoComponent } from './component/contacto/contacto.component';
import { NosotrosComponent } from './component/nosotros/nosotros.component';
import {HttpClientModule} from '@angular/common/http';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';



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
    CarritoComponent,
    ContactoComponent,
    NosotrosComponent
     ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
