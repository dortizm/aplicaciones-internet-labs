document.getElementById("btnLoadData").addEventListener("click", function() {
    // Llamada a la API utilizando AJAX con JavaScript puro
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Procesar la respuesta de la API
            var response = JSON.parse(xhr.responseText);
            mostrarDatos(response);
        }
    };

    // Establecer la solicitud GET a la API de FilmOn
    xhr.open("GET", "https://filmon.com/page/api-vod", true);
    xhr.send();
});

function mostrarDatos(data) {
    // Aquí puedes procesar y mostrar los datos en el formato que desees
    var resultContainer = document.getElementById("result");
    resultContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
}
