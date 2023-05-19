import { Injectable } from '@angular/core';
import { Producto } from '../model/producto.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  private Api_back = "http://localhost:3000/Producto01";

  //producto:Producto[]=[];
  

 /* agregarProductoService(producto:Producto){

    this.producto.push(producto);
  }
*/

  constructor(private http: HttpClient) { }

  public getTodosProductos(): Observable<any>{
    return this.http.get(this.Api_back);
  }
}
