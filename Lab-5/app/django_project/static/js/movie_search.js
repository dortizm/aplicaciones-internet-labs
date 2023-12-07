$(document).ready(function() {
    // Llena dinámicamente el selector de géneros al cargar la página
    // Puedes obtener la lista de géneros de la API al inicio si lo prefieres
    // (esto requerirá una llamada inicial a la API)

    // Realiza una llamada AJAX cuando cambia el género seleccionado
    $("#genre").change(function() {
        var selectedGenre = $(this).val();
        var apiUrl = "http://api.filmon.com/api/vod/search?genre=" + selectedGenre;

        $.ajax({
            url: apiUrl,
            type: "GET",
            success: function(data) {
                // Maneja la respuesta de la API y actualiza la tabla
                updateTable(data);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });

    // Función para actualizar la tabla con datos de la API
    function updateTable(data) {
        // Implementa la lógica para actualizar la tabla con los datos recibidos
    }
});
