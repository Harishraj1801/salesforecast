import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/Services/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm;
  details = { email: "", password: "" };

  constructor(private snackBar: MatSnackBar,private router: Router, private auth: AuthService, private fb: FormBuilder, private http: HttpClient) { 
    this.loginForm = fb.group({
      email:['', [Validators.required, Validators.email, Validators.pattern('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,63}$')]],
      password: ['', [Validators.required, Validators.pattern('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).+$')]]
    });
  }

  ngOnInit(): void {
  }

  get email(){
    return this.loginForm.get('email');
  }

  get password(){
    return this.loginForm.get('password');
  }

  onSubmit(email:any,password:any){
    console.log(email,"email")
    console.log(password,"password")
    
    this.details.email = email;
    this.details.password = password;

    const headers = new HttpHeaders().set('Content-Type', 'application/json');
     this.http.post<any>('http://localhost:5000/verify', this.details, { headers: headers }).subscribe(data => {
        console.log(data);
        if (data.exists) {
          //alert('User LOGGED In');
          this.snackBar.open("User Logged in", "Ok", { duration: 3000 });
          this.auth.sendToken(this.details.email)
          this.router.navigate(['/upload'])
        } else {
            //alert('Incorrect email or password.');
            this.snackBar.open("Incorrect email or password", "Ok", { duration: 3000 });
            this.router.navigate(['/login']);
        }
    });
  
  }

}
