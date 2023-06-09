import { Injectable } from '@angular/core';
import { Producto } from '../model/producto.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  private Api_back = "http://localhost:8000/api/";



  constructor(private http: HttpClient) { }

  public getTodosProductos(): Observable<any>{
    /*return this.http.get(this.Api_back+ "productos");*/
    return this.http.get('api/productos');
  }

  public detalle(id:number): Observable<any>{
    return this.http.get<any>('api/productos/'+ id);
  }

  public postProductos(productData: any): Observable<any>{
    return this.http.post('api/productos/', productData);
  }

  public save(producto:Producto): Observable<any>{
    return this.http.post<any>(`api/productos/`,producto);
  }
  public update(cod: number,producto:Producto ): Observable<any>{
    return this.http.post<any>(`api/agregarproductos/${cod}`,producto);
  }
  public borrar(cod: number): Observable<any>{
    return this.http.delete<any>(`api/productos/${cod}`);
  }

  
}
