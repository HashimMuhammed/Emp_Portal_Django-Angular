import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIurl="http://127.0.0.1:8000";
readonly Photourl="http://127.0.0.1:8000/media/"
  constructor(private http:HttpClient) { }
  getDepList():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl+'/department/');
  }
  addDep(val:any){
    return this.http.post(this.APIurl+'/department/',val);
  }
  updateDep(val:any){
    return this.http.put(this.APIurl+'/department/',val);
  }
  deleteDep(val:any){
    return this.http.delete(this.APIurl+'/department/'+val);
  }

  uploadPhoto(val:any){
    return this.http.post(this.APIurl+'/Savefile',val);
  }
  getAllDepartmentNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl+'/department/');
  }
  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIurl+'/employee/');
  }
  addEmp(val:any){
    return this.http.post(this.APIurl+'/employee/',val);
  }
  updateEmp(val:any){
    return this.http.put(this.APIurl+'/employee/',val);
  }
  deleteEmp(val:any){
    return this.http.delete(this.APIurl+'/employee/'+val);
  }

}
