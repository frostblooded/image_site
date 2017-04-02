import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {RouterModule} from '@angular/router';
import {FacebookModule} from './oauth/facebook/facebook.module';
import {NavbarModule} from './navbar/navbar.module';

@NgModule({
  imports:      [
    BrowserModule,
    RouterModule.forRoot([]),
    FacebookModule,
    NavbarModule,
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
