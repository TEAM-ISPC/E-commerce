import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

  formUser = new FormGroup({

    'nombre' : new FormControl('', [Validators.required]),
    'apellido' : new FormControl('', [Validators.required]),
    'telefono' : new FormControl('', [Validators.required]),
    'correo' : new FormControl('', [Validators.required, Validators.email]),
    'password' : new FormControl('', [Validators.required, Validators.minLength(6)]),
    'password2' : new FormControl('', [Validators.required])

  })
  get nombre(){
    return this.formUser.get('nombre') as FormControl;
    
  }
  get apellido(){
    return this.formUser.get('apellido') as FormControl;
  }
  get telefono(){
    return this.formUser.get('telefono') as FormControl;
  }
  get correo(){
    return this.formUser.get('correo') as FormControl;
  }
  get password(){
    return this.formUser.get('password') as FormControl;
  }
  get password2(){
    return this.formUser.get('password2') as FormControl;
  }

  

  ngOnInit(): void {
    
  }

}
