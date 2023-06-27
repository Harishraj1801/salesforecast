import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { User } from '../Components/sales-forecast/user';

@Injectable({
  providedIn: 'root'
})
export class SalesForecastService {

  baseApiUrl  = "http://localhost:5000/forecast"

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  upload(user: User){
    this.snackBar.open("Forecast period is selected", "Ok", { duration: 50000 });
    return this.http.post<any>(
      this.baseApiUrl,
      user
    )
  }
}
