import { Component, OnInit } from '@angular/core';
import { Producto } from 'src/app/model/producto.model';
import { ProductoService } from 'src/app/service/producto.service';

@Component({
  selector: 'app-tienda',
  templateUrl: './tienda.component.html',
  styleUrls: ['./tienda.component.css']
})
export class TiendaComponent implements OnInit {

  constructor(private miProducto:ProductoService){
    
  }
  ngOnInit(): void {
    this.producto=this.miProducto.producto
  }

  producto:Producto[]=[];


}
