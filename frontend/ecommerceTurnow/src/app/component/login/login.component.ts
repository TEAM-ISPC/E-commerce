import { NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormControl,  NgForm, Validators } from '@angular/forms';
import { LoginService } from 'src/app/service/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent  implements OnInit {

  correo = new FormControl ('',[Validators.required,Validators.email]);
  password = new FormControl ('');




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
