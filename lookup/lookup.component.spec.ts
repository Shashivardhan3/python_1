import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StagebankComponent } from './lookup.component';

describe('StagebankComponent', () => {
  let component: StagebankComponent;
  let fixture: ComponentFixture<StagebankComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StagebankComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StagebankComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
