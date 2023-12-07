// static/js/script.js
$(document).ready(function () {
    $('#genres').change(function () {
        var selectedGenre = $(this).val();
        if (selectedGenre) {
            $.ajax({
                url: `/get_movies/${selectedGenre}/`,
                method: 'GET',  // Agregamos 'method' para mayor claridad
                dataType: 'json',  // Especificamos el tipo de datos esperado
                success: function (data) {
                    console.log('Respuesta de la API:', data);

                    // Limpia el cuerpo de la tabla antes de agregar nuevas filas
                    $('#moviesTableBody').empty();

                    // Verifica si la respuesta tiene la propiedad "movies" y es un array
                    if (data.movies && Array.isArray(data.movies)) {
                        // Agrega las filas de películas si hay datos
                        $.each(data.movies, function (index, movie) {
                            var newRow = '<tr>' +
                                '<td>' + movie.title + '</td>' +
                                '<td>' + movie.description + '</td>' +
                                '<td><img src="' + movie.poster.url + '" style="width: 50px; height: 50px;"></td>' +
                                '<td><a href="' + movie.slug + '">Detalles</a></td>' +
                                '</tr>';
                            $('#moviesTableBody').append(newRow);
                        });
                    } else {
                        // Si no hay datos, mostrar un mensaje en la consola
                        console.log('No hay películas disponibles para este género.');
                    }
                },
                error: function (xhr, status, error) {
                    console.error('Error en la solicitud:', status, error);
                }
            });
        } else {
            // Limpiar el cuerpo de la tabla si no se selecciona ningún género
            $('#moviesTableBody').empty();
        }
    });
});
