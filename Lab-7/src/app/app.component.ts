import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Genre {
  slug: string;

}

interface SearchResponse {
  response: any[]; 
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  genres: string[] = [];
  selectedGenre: string = '';
  responseData: any[] = [];

  constructor(private http: HttpClient) {
    this.getGenres();
  }

  getGenres() {
    this.http.get<{ response: Genre[] }>('http://api.filmon.com/api/vod/genres')
      .subscribe(
        (data) => {
          console.log('API Response:', data);
          this.genres = data.response.map((genre) => genre.slug);
          console.log('Genres:', this.genres);
        },
        (error) => {
          console.error('Error fetching genres:', error);
          
        }
      );
  }

  onGenreSelected(event: any) {
    this.selectedGenre = event.target.value;

    if (this.selectedGenre) {
      this.http.get<SearchResponse>(`http://api.filmon.com/api/vod/search?genre=${this.selectedGenre}`)
        .subscribe(
          (data) => {
            console.log('API Search Response:', data);
            this.responseData = data.response;
            console.log('Response Data:', this.responseData);
          },
          (error) => {
            console.error('Error fetching search results:', error);
            
          }
        );
    }
  }
}


