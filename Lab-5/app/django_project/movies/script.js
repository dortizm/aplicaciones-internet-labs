// script.js
$(document).ready(function() {
    $('#genre').change(function() {
        var selectedGenre = $(this).val();
        $.ajax({
            url: 'http://api.filmon.com/api/vod/search?genre=' + selectedGenre,
            method: 'GET',
            success: function(data) {
                // Manipula los datos recibidos y actualiza la tabla movies-table en el HTML
                actualizarTabla(data);
            },
            error: function(error) {
                console.log(error);
            }        });
    });

    function actualizarTabla(data) {
        // Implementa lógica para actualizar la tabla con los datos de la API
        // Puedes utilizar jQuery o JavaScript puro para esto
    }
});
