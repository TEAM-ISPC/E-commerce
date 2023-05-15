import { Injectable } from '@angular/core';
import { Producto } from '../model/producto.model';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {



  producto:Producto[]=[];
  

  agregarProductoService(producto:Producto){

    this.producto.push(producto);
  }


  constructor() { }
}
