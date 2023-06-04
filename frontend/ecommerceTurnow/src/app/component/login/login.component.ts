import { NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormControl,  FormGroup,  NgForm, Validators } from '@angular/forms';
import { LoginService } from 'src/app/service/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent  implements OnInit {

  get correo(){
    return this.formUser.get('correo') as FormControl;
  }

  get password(){
    return this.formUser.get('password') as FormControl;
  }

  formUser =new FormGroup({

    'correo' : new FormControl ('',[Validators.required,Validators.email]),
    'password' : new FormControl ('',Validators.required)
  });

 



  constructor() { 

  }

  ngOnInit(): void {

   }

  /*login(form: NgForm){

    const email=form.value.email

    const password=form.value.password

  //  this.loginService.login(email, password);

  }  */

}
