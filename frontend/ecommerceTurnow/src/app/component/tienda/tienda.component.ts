import { Component, OnInit } from '@angular/core';
import { ProductoService } from 'src/app/service/producto.service';

@Component({
  selector: 'app-tienda',
  templateUrl: './tienda.component.html',
  styleUrls: ['./tienda.component.css']
})
export class TiendaComponent implements OnInit {

  producto: any={};

  constructor(private miProducto:ProductoService){
    
  }


  ngOnInit(): void {
    this.miProducto.getTodosProductos().subscribe(resp =>{
      this.producto = resp;
     
      
    })
    
  }

  


}
