import { Component, OnInit, ViewChild, TemplateRef } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { HttpClient } from '@angular/common/http';
import { DatatableComponent, id } from '@swimlane/ngx-datatable';
import {
  UntypedFormGroup,
  UntypedFormBuilder,
  UntypedFormControl,
  Validators,
} from '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ToastrService } from 'ngx-toastr';
import Swal from 'sweetalert2';
import { Router } from '@angular/router';
import { __values } from 'tslib';
import { cB, cb } from '@fullcalendar/core/internal-common';


@Component({
  selector: 'app-lookup',
  templateUrl: './lookup.component.html',
  // styleUrls: ['./lookup.component.sass'],
  providers: [ToastrService],
})
export class LookupComponent implements OnInit {
  @ViewChild(DatatableComponent, { static: false }) table: DatatableComponent;
  rows = [];
  scrollBarHorizontal = window.innerWidth < 1200;
  selectedRowData: selectRowInterface;
  newUserImg = 'assets/images/users/user-2.png';
  data = [];
  filteredData = [];
  BankdataSource = new MatTableDataSource();
  expanded = true;
  editForm: UntypedFormGroup;
  register: UntypedFormGroup;
  loadingIndicator = true;
  isRowSelected = false;
  selectedOption: string;
  reorderable = true;
  public selected: any[] = [];
  columns = [
    // { name: 'bankid' },
    { name: 'bankname' },
    { name: 'bankaccno' },
    { name: 'userid' },
    { name: 'companyid' },
    { name: 'ifsccode' },
    { name: 'swiftcode' },
    { name: 'contactid' },
    // { name: 'ContactAddress' },
    // { name: 'createdby' },
    // { name: 'modifiedby' },
  ];
  documenttype = [
    { id: '1', value: 'Statutory' },
    { id: '2', value: 'Certificates' },
    { id: '3', value: 'Experience' },
  
  ];
  certificates = [
    { id: '1', value: 'SSLC' },
    { id: '2', value: 'PUC' },
    { id: '3', value: 'Degree' },
    { id: '4', value: 'MasterDegree' },
    { id: '5', value: 'PHD' },
  ] ;
  experiences = [
    { id: '1', value: 'ExperienceLetter' },
    { id: '2', value: 'ReleievingLetter' },
   
  ] ;

  // genders = [
  //   { id: '1', value: 'male' },
  //   { id: '2', value: 'female' },
  // ];
  // statusType = [
  //   { id: '1', value: 'Active' },
  //   { id: '2', value: 'Completed' },
  //   { id: '3', value: 'Pending' },
  // ];
  // designationType = [
  //   { id: '1', value: 'Manager' },
  //   { id: '2', value: 'Team Leader' },
  //   { id: '3', value: 'Clerk' },
  // ];
  @ViewChild(DatatableComponent, { static: false }) table2: DatatableComponent;
  apiServer: string;
  httpClient: any;
  dataService: any;
  isEditable: any;
  renderer: any;
  isLocked: boolean = true;
  constructor(
    private fb: UntypedFormBuilder,
    private modalService: NgbModal,
    private toastr: ToastrService,
    private http: HttpClient,
  ) {
    this.editForm = this.fb.group({
      // id: new UntypedFormControl(),
      // img: new UntypedFormControl(),
      // bankid: new UntypedFormControl(),
      bankname: new UntypedFormControl(),
      bankaccno: new UntypedFormControl(),
      userid: new UntypedFormControl(),
      companyid: new UntypedFormControl(),
      ifsccode: new UntypedFormControl(),
      swiftcode: new UntypedFormControl(),
      contactid: new UntypedFormControl(),
      // ContactAddress: new UntypedFormControl(),
      // createdby: new UntypedFormControl(),
      // modifiedby: new UntypedFormControl(),
    });
    window.onresize = () => {
      this.scrollBarHorizontal = window.innerWidth < 1200;
    };
  }
  // select record using check box
  onSelect({ selected }) {
    this.selected.splice(0, this.selected.length);
    this.selected.push(...selected);

    if (this.selected.length === 0) {
      this.isRowSelected = false;
    } else {
      this.isRowSelected = true;
    }
  }
  deleteSelected() {
    Swal.fire({
      title: 'Are you sure?',
      showCancelButton: true,
      confirmButtonColor: '#8963ff',
      cancelButtonColor: '#fb7823',
      confirmButtonText: 'Yes',
    }).then((result) => {
      if (result.value) {
        this.selected.forEach((row) => {
          this.deleteRecord(row);
        });
        this.deleteRecordSuccess(this.selected.length);
        this.selected = [];
        this.isRowSelected = false;
      }
    });
  }
  ngOnInit() {
    this.fetch((data) => {
      this.data = data;
      this.filteredData = data;
      setTimeout(() => {
        this.loadingIndicator = false;
      }, 500);
    });
       // Fetch data from the banks API
  this.http.get('http://59.90.29.10:44444/api/lookups/lookuptype/').subscribe((data: any[]) => {
    this.BankdataSource.data = data;
  });
    
    this.register = this.fb.group({
      id: [''],
      img: [''],
      // bankid: [''],
      bankname: [''],
      bankaccno: ['', [Validators.required, Validators.pattern('[a-zA-Z]+')]],
      userid: [''],
      companyid: ['', [Validators.required]],
      ifsccode: ['', [Validators.required]],
      swiftcode: ['', [Validators.required]],
      contactid: ['', [Validators.required, Validators.email, Validators.minLength(5)]],
      // ContactAddress: ['', [Validators.required]],
      // createdby: [''],
      // modifiedby: [''],
    });
    // this.data = this.dataService.getDataById(id); // Get the data to be edited from the service
    // this.editForm.patchValue(this.data);

  }

  // fetch data
  fetch(cb) {
    const req = new XMLHttpRequest();
    req.open('GET', 'http://59.90.29.10:44444/api/lookups/');
    req.onload = () => {
      const data = JSON.parse(req.response);
      cb(data);
    };
    req.send();
  }

  // add new record
  addRow(content) {
    this.modalService.open(content, {
      ariaLabelledBy: 'modal-basic-title',
      size: 'lg',
    });
    this.register.patchValue({
      id: this.getId(10, 100),
      img: this.newUserImg,
    });
  }
  // edit record
  editRow(row, rowIndex, content) {
    this.modalService.open(content, {
      ariaLabelledBy: 'modal-basic-title',
      size: 'lg',
    });
    this.editForm.setValue({
      // id: row.id,
      // img: row.img,
      // bankid: row.bankid,
      bankname: row.bankname,
      bankaccno: row.bankaccno,
      userid: row.userid,
      companyid: row.companyid,
      ifsccode: row.ifsccode,
      swiftcode: row.swiftcode,
      contactid: row.contactid,
      // ContactAddress: row.ContactAddress,
      // createdby: row.createdby,
      // modifiedby: row.modifiedby,
    });
    this.selectedRowData = row;


  }
  // delete single row
  deleteSingleRow(row) {
    Swal.fire({
      title: 'Are you sure?',
      showCancelButton: true,
      confirmButtonColor: '#8963ff',
      cancelButtonColor: '#fb7823',
      confirmButtonText: 'Yes',
    }).then((result) => {
      if (result.value) {
        this.deleteRecord(row);
        this.deleteRecordSuccess(1);
      }
    });
  }

  deleteRecord(row) {
    this.data = this.data.filter(r => r !== row);
    this.http.delete(`http://59.90.29.10:44444/api/lookups${row.bankid}`).subscribe(() => {
      this.data = this.data.filter(r => r !== row);
    });
  }

  getdata() {
    throw new Error('Method not implemented.');

  }
  arrayRemove(array, id) {
    return array.filter(function (element) {
      return element.id !== id;
    });
  }
  // save add new record
  onAddRowSave(form: UntypedFormGroup) {
    // console.log(form.value)
    // this.data.push(form.value);
    // this.data = [...this.data];
    // form.reset();
    // this.modalService.dismissAll();
    // this.addRecordSuccess();
    this.http.post('http://59.90.29.10:44444/api/lookups', form.value).subscribe(() => {
      // Successfully saved data
      this.data.push(form.value);
      this.data = [...this.data];
      form.reset();
      this.modalService.dismissAll();
      this.addRecordSuccess();
    }, (error) => {
      // Handle error saving data
      console.error(error);
    });
    // this.data = this.dataService.getDataById(id); // Get the data to be edited from the service
    // this.editForm.patchValue(this.data);

  }

  httpOptions<T>(arg0: string, arg1: string, httpOptions: any) {
    throw new Error('Method not implemented.');
  }
  // save record on edit
  onEditSave(form: UntypedFormGroup) {
    const record = form.value;
    this.http.put(`http://59.90.29.10:44444/api/lookups${record.lookups}`, record).subscribe(() => {
      this.data = this.data.map((value) => {
        if (value.baakid == record.bankid) {
          return record;
        }
        return value;
      });
      const index = this.data.findIndex((value) => value.lookups == record.lookups);
      this.data[index] = record;

      this.modalService.dismissAll();
      this.editRecordSuccess();
    }, (error) => {
      // Handle error updating data
      console.error(error);
      this.editRecordSuccess();
      this.modalService.dismissAll();
    });
    // this.data = this.data.filter((value, key) => {
    //   if (value.id == form.value.id) {
    //     value.bankid = form.value.bankid;
    //     value.bankname = form.value.bankname;
    //     value.bankaddress = form.value.bankaddress;
    //     value.bankaccno = form.value.bankaccno;
    //     value.bobjid = form.value.bobjid;
    //     value.bobjname = form.value.bobjname;
    //     value.ifsccode = form.value.ifsccode;
    //     value.swiftcode = form.value.swiftcode;

    //   }
    //   this.modalService.dismissAll();
    //   return true;
    // });
    // this.editRecordSuccess();
  }

  // filter table data
  filterDatatable(event) {
    // get the value of the key pressed and make it lowercase
    const val = event.target.value.toLowerCase();
    // get the amount of columns in the table
    const colsAmt = this.columns.length;
    // get the key names of each column in the dataset
    const keys = Object.keys(this.filteredData[0]);
    // assign filtered matches to the active datatable
    this.data = this.filteredData.filter(function (item) {
      // iterate through each row's column data
      for (let i = 0; i < colsAmt; i++) {
        // check for a match
        if (
          item[keys[i]].toString().toLowerCase().indexOf(val) !== -1 ||
          !val
        ) {
          // found match, return true to add to result set
          return true;
        }
      }
    });
    // whenever the filter changes, always go back to the first page
    this.table.offset = 0;
  }
  // get random id
  getId(min, max) {
    // min and max included
    return Math.floor(Math.random() * (max - min + 1) + min);
  }
  addRecordSuccess() {
    this.toastr.success('Add Record Successfully', '');
  }
  editRecordSuccess() {
    this.toastr.success('Edit Record Successfully', '');
  }
  deleteRecordSuccess(count) {
    this.toastr.error(count + ' Records Deleted Successfully', '');
  }
}
export interface selectRowInterface {
  // img: String;
  firstName: String;
  // lastName: String;
}
