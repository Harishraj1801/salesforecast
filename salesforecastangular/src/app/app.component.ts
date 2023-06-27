import { Component } from '@angular/core';
import { faArrowTrendUp } from '@fortawesome/free-solid-svg-icons'
import { AuthService } from './Services/auth.service';
import { HostListener } from '@angular/core';
import { Route } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  constructor(private auth: AuthService){} 
  @HostListener('window:beforeunload')
  clearStorage1(){
    this.auth.logout();
    alert("logged out");
  }

  onClick(){
    this.auth.logout();
    alert("logged out");
  }

  title = 'sales-forecast';
  arrow = faArrowTrendUp;

  
}
