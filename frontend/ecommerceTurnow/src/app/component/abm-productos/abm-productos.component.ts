import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductoService } from 'src/app/service/producto.service';



@Component({
  selector: 'app-abm-productos',
  templateUrl: './abm-productos.component.html',
  styleUrls: ['./abm-productos.component.css']
})
export class AbmProductosComponent implements OnInit {
  producto: any={};
  isLogged: boolean=true;

  
  constructor(private miProducto:ProductoService ,private activatedRouter: ActivatedRoute, private router: Router){
    
  }


  ngOnInit(): void {
    let id = this.activatedRouter.snapshot.params['id'];
    console.log("id "+id)
    this.miProducto.detalle(id).subscribe(
      data => {
        this.producto = data;
      }, err => {
        alert("Error de comunicación");
        this.router.navigate(['']);
      }
    )
    
    
  }
  eliminar(codigodeBarras: number){
    this.miProducto.borrar(codigodeBarras).subscribe(
      data =>{this.producto()}
    )

  }

  modificar(): void{
    const id = this.activatedRouter.snapshot.params['id'];
    this.miProducto.update(id, this.producto).subscribe(
      data => {
        this.router.navigate(['']);
      }, err =>{
         alert("Error al modificar ");
         this.router.navigate(['']);
      }
    )
  }


}
