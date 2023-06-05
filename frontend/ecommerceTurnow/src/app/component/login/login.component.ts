import { Component, OnInit } from '@angular/core';
import { FormControl, FormBuilder,  FormGroup,  NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/service/login.service';
import { RequestStatus } from 'src/app/model/statusrequest';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent  implements OnInit {

  form = this.formBuilders.group({
    correo: ['', [Validators.email, Validators.required, Validators.pattern('^\\w+([.-]?\\w+)*@\\w+([.-]?\\w+)*(\\.\\w{2,3})+$')
  ]],
    password: ['', Validators.required],
  })
  status: RequestStatus = 'init'

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

 



  constructor(
    private loginService: LoginService,
    private formBuilders: FormBuilder,
    private router: Router
  ) { 

  }

  ngOnInit(): void {

   }

   login(e: Event) {
    e.preventDefault()
    if(this.form.valid){
      this.status = 'loading'
      const {correo, password} = this.form.getRawValue()
      this.loginService.login(correo as string, password as string)
      .subscribe({
        next: (s) => {
          this.status = 'success'
          this.router.navigate(['/home'])
        },
        error: () => {
          this.status = 'failed'
          setTimeout(() => {
            this.status = 'init'
          }, 2000)
          console.log('error')
        }
      })
      console.log(this.form.value)
    }else {
      this.form.markAllAsTouched()
    }
   }

}
