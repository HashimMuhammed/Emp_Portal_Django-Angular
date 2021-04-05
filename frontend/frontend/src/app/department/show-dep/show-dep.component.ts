import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {
 
  constructor(private service:SharedService) { }
  depList:any=[];
  ModalTitle: any;
  ActivateAddDepComp:boolean=false;
  dep:any;

  addClick(){
    this.dep={
      DepartmentId:0,
      DepartmentName:""
    }
    this.ModalTitle="Add Department"
    this.ActivateAddDepComp=true;
  }
  closeClick(){
    this.ActivateAddDepComp=false
    this.refreshDepList()
  }
  editClick(item:any){
    this.dep=item;
    this.ModalTitle="Edit Department"
    this.ActivateAddDepComp=true;

  }

  deleteClick(item:any){
    if(confirm("Are you sure")){
      this.service.deleteDep(item.DepartmentId).subscribe(data=>
        {
          alert(data.toString());
          this.refreshDepList();
        })
    }
  }


  ngOnInit(): void {
    this.refreshDepList();
  }
  
refreshDepList(){
  this.service.getDepList().subscribe(data=>{
    this.depList=data;
  });
}

}
