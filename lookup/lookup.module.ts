import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LookupRoutingModule } from './lookup-routing.module';
import { LookupComponent } from './lookup.component';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { ToastrModule } from 'ngx-toastr';

@NgModule({
  declarations: [LookupComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    LookupRoutingModule,
    NgxDatatableModule,
    ToastrModule.forRoot(),
  ],
})
export class LookupRoutingModule {}
