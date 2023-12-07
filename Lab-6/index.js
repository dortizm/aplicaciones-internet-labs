
var app = angular.module('miApp', ['ngRoute']);

app.config(
    function ($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'index.html',
                controller: 'miControlador'
            }).
            when('/movie/:id', {
                templateUrl: 'movie.html',
                controller: 'DetallePeliculaController'
            });
    });

app.controller('miControlador', function ($scope, $http) {
    $scope.selectedGenre = "";
    $scope.generos = [];
    $scope.peliculas = [];

    $http.get('http://api.filmon.com/api/vod/genres')
        .then(function (response) {
            $scope.generos = response.data.response;
        });

    $scope.obtenerPeliculas = function () {
        var url = 'http://api.filmon.com/api/vod/search?genre=' + $scope.selectedGenre;
        $http.get(url)
            .then(function (response) {
                $scope.peliculas = response.data.response;
            });
    };

    $scope.obtenerDetallePelicula = function (movie) {
        window.location.href = 'movie.html?id=' + movie.id;
    };
});

app.controller('DetallePeliculaController', function ($scope, $routeParams, $http) {
    var peliculaId = $routeParams.id;
    $scope.detallePelicula = {
        id: peliculaId,
        title: 'Ejemplo de Película',
        year: 2022,
        genre: 'Acción',
        length: '2h 30min'
    };
});