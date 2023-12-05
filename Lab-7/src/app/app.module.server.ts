import { NgModule } from '@angular/core';
import { ServerModule } from '@angular/platform-server';
import { AppModule } from './app.module';


@NgModule({
  imports: [AppModule, ServerModule],
  bootstrap: [AppModule],
})
export class AppServerModule {}

