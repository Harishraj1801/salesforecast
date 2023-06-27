import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './Components/login/login.component';
import { FileUploadComponent } from './Components/file-upload/file-upload.component';
import { SalesForecastComponent } from './Components/sales-forecast/sales-forecast.component';
import { AuthGuard } from './Services/auth.guard';

const routes: Routes = [
  {
    path: "login",
    component: LoginComponent,
    
  },
  {
    path: "upload",
    component: FileUploadComponent,
    canActivate:[AuthGuard]
  },
  {
    path: "forecast",
    component: SalesForecastComponent,
  },
  {
    path: "",
    component: LoginComponent
  }
];

@NgModule( {
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [AuthGuard]
})
export class AppRoutingModule { }
