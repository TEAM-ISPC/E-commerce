import { Component, OnInit } from '@angular/core';
import { Form, FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductoService } from 'src/app/service/producto.service';

@Component({
  selector: 'app-publicar-producto',
  templateUrl: './publicar-producto.component.html',
  styleUrls: ['./publicar-producto.component.css']
})
export class PublicarProductoComponent {
    productForm = this.formBuilder.group({
      nombreProducto: ['', Validators.required],
      descripcionProducto: ['', Validators.required],
      precioUnitario: ['', Validators.required],
      cantidadProducto: ['', Validators.required],
      imagenProducto: ['', Validators.required],
      idCategoria: ['', Validators.required],
    })
  
    constructor(
      private formBuilder: FormBuilder,
      private productService : ProductoService,
    ) {}
  
    get nombreProducto() {
      return this.productForm.controls.nombreProducto;
    }
    get descripcionProducto() {
      return this.productForm.controls.descripcionProducto;
    }
    get precioUnitario() {
      return this.productForm.controls.precioUnitario;
    }
    get cantidadProducto() {
      return this.productForm.controls.cantidadProducto;
    }
    get imagenProducto() {
      return this.productForm.controls.imagenProducto;
    }
    get idCategoria() {
      return this.productForm.controls.idCategoria;
    }
  
    crearProducto() {
      if (this.productForm.valid) {
        this.productService.postProductos(this.productForm.value).subscribe({
          error: (errorData) => {
            console.error(errorData);
          },
          complete: () => {
            console.log("Producto creado");
          }
        })
      }else {
        this.productForm.markAllAsTouched();
        alert('No se permiten campos vacios.');
      }
    }
  
}
