import { HttpClient } from '@angular/common/http';
/*import { Token } from '@angular/compiler';*/
import { Injectable } from '@angular/core';
import { Router } from 'express';
import { tap } from 'rxjs';
import { TokenService } from './token.service';
import { Token } from '../model/token.model';






@Injectable({
  providedIn: 'root'
})
export class LoginService {
  apiUrl = 'http://localhost:8000/'
  constructor(
    private http: HttpClient,
    private tokenService: TokenService
  ) { }

  login(email: string, password: string) {
    return this.http.post<Token>(`${this.apiUrl}login`, {
      email,
      password
    })
      .pipe(
        tap(resp => {
          this.tokenService.createToken(resp.access_token)
        })
      )
  }



}

 // getIdToken(){

  //  return this.token;
//  }
//}
