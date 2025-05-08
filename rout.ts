import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SpamClassifierService {
  private apiUrl = 'http://127.0.0.1:5000/predict'; // or your deployed URL

  constructor(private http: HttpClient) {}

  predictMessage(message: string): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });

    const body = new URLSearchParams();
    body.set('message', message);

    return this.http.post(this.apiUrl, body.toString(), { headers });
  }
}
