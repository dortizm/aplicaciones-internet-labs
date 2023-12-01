// main.js
$(document).ready(function() {
    // Referencias a elementos HTML
    var genreSelect = $('#genres');
    var movieTable = $('.table tbody');

    // Función para cargar géneros desde la API
    function cargarGeneros() {
        
        $.ajax({
            url: 'http://api.filmon.com/api/vod/genres',
            method: 'GET',
            success: function(response) {
                // Limpia el select antes de agregar nuevos géneros
                genreSelect.empty();

                // Agrega opciones al select con los géneros obtenidos
                for (var i = 0; i < response.length; i++) {
                    var genre = response[i];
                    genreSelect.append('<option value="' + genre.id + '">' + genre.name + '</option>');
                }
            },
            error: function(error) {
                console.error('Error al cargar géneros:', error);
            }
        });
    }

    // Función para cargar películas por género desde la API
    function cargarPeliculasPorGenero(genreId) {
        $.ajax({
            url: 'http://api.filmon.com/api/vod/search',
            method: 'GET',
            data: {
                genre: genreId
            },
            success: function(response) {
                // Limpia la tabla antes de agregar nuevas filas
                movieTable.empty();

                // Agrega filas a la tabla con la información de las películas
                for (var i = 0; i < response.length; i++) {
                    var movie = response[i];
                    movieTable.append('<tr><td>' + movie.title + '</td><td>' + movie.description + '</td><td><img src="' + movie.image + '" style="width:50px; height:75px;"></td><td><a href="' + movie.details_link + '">Detalles</a></td></tr>');
                }
            },
            error: function(error) {
                console.error('Error al cargar películas:', error);
            }
        });
    }

    // Cargar géneros al cargar la página
    cargarGeneros();

    // Manejar cambio en el selector de géneros
    genreSelect.on('change', function() {
        // Obtener el ID del género seleccionado
        var selectedGenreId = genreSelect.val();

        // Cargar películas por el género seleccionado
        cargarPeliculasPorGenero(selectedGenreId);
    });
});
