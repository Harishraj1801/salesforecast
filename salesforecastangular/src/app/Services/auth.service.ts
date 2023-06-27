import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private router: Router) { }

  sendToken(token: string){
    localStorage.setItem("LoggedInUser", token)
  }

  getToken(){
    return localStorage.getItem("LoggedInUser")
  }
  
  IsLoggedIn(){
    return this.getToken() !== null;
  }

  logout(){
    localStorage.clear();
    //this.router.navigate(["login"])
  }
}
