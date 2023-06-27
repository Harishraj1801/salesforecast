import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { SalesForecastService } from 'src/app/Services/sales-forecast.service';
import { User } from './user';

@Component({
  selector: 'app-sales-forecast',
  templateUrl: './sales-forecast.component.html',
  styleUrls: ['./sales-forecast.component.css']
})
export class SalesForecastComponent implements OnInit {

  
  userModel = new User('');
  
  dates: any[] = [
    '6',
    '12',
    '24',
    '60'
  ];

  constructor(private forecastServie: SalesForecastService) { }


  ngOnInit(): void {
  }
  
  onSubmit(){
     console.log(this.userModel);  
     this.forecastServie.upload(this.userModel)
         .subscribe(
           data => console.log('Success',data)
         )
  }

  routeToMl(){
    window.location.href = "http://127.0.0.1:5000/plot";
  }
}
