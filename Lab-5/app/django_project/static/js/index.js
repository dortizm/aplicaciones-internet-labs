var selectGeneros = $('#generos');

$(document).ready(function () {
    
    $.ajax({
        url: "http://api.filmon.com/api/vod/genres",
        type: "GET",
        dataType: "json",
        success: function (data) {
            
            if (data && data.response && data.response.length > 0) {
                data.response.forEach(function(genero) {
                    selectGeneros.append($('<option>', {
                        value: genero.id,
                        text: genero.name,
                        slug: genero.slug
                    }));
                });
            } else {
                console.log('No se encontraron géneros de películas.');
            }
        },
        error: function(error) {
            console.error('Error al obtener los géneros:', error);
        }
    });

    var tabla = $('#ipi-table tbody');

    selectGeneros.change(function () {
        
        var selectedGenre = $(this).find('option:selected').attr('slug');
        
        $('#tipo').text($(this).find('option:selected').text());

        $.ajax({
            url: 'http://api.filmon.com/api/vod/search?genre=' + selectedGenre,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
    
                tabla.empty();
                data.response.forEach(function (pelicula) {
                    var row = $('<tr>');
                    row.append($('<td>').text(pelicula.title));
                    row.append($('<td>').text(pelicula.description));

                    var imgTd = $('<td>');
                    var img = $('<img>');
                    img.attr('src', pelicula.poster.url);
                    img.attr('alt', pelicula.title);
                    img.addClass('img-fluid'); 
                    img.css('max-width', '175px');
                   
                    img.click(function() {
                        window.location.href = pelicula.poster.url;
                    });
                    
                    img.hover(function() {
                        $(this).css('cursor', 'pointer');
                    });
                    imgTd.append(img);
                    row.append(imgTd);

                    console.log(pelicula.produced_date);

                    var producedDate = moment(pelicula.produced_date).format("D [de] MMMM [de] YYYY");
                
                    if (producedDate == "Invalid date") {
                        producedDate = "Fecha de producción: Desconocida";
                    }
                    row.append($('<td>').text("Fecha de producción: " + producedDate));

                    tabla.append(row);
                });
            },
            error: function (error) {
                console.error('Error al obtener las películas:', error);
            }
        });
    });
});