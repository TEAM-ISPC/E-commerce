import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductoService } from 'src/app/service/producto.service';

@Component({
  selector: 'app-item-tienda',
  templateUrl: './item-tienda.component.html',
  styleUrls: ['./item-tienda.component.css']
})
export class ItemTiendaComponent implements OnInit{
  items: any={};

  constructor(private  misItems: ProductoService,private activatedRouter: ActivatedRoute, private router: Router){}
  
  
  ngOnInit(): void {
    let id = this.activatedRouter.snapshot.params['id'];
    console.log("id "+id)
    this.misItems.detalle(id).subscribe(
      data => {
        this.items = data;
      }, err => {
        alert("Error de comunicación");
        this.router.navigate(['']);
      }
    )
  }

}
