import { Injectable } from '@angular/core';
import {setCookie, getCookie, removeCookie} from 'typescript-cookie';


@Injectable({
  providedIn: 'root'
})
export class TokenService {

  constructor() { }

  createToken(token: string) {
    setCookie('token', token, {expires:365, path:"/"})
  }

  getToken() {
    const token = getCookie('token');
    return token;
  }

  removeToken() {
    removeCookie('token')
  }
}
