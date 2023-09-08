<!DOCTYPE html>
<html lang="es">
<head>
        <title>Aplicaciones de Internet</title>
        <meta charset="utf-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    </head>
<body>
<?php
 echo "hola";
?>
    <div class="container">
        <div class="row">
            <h1>Aplicaciones de Internet</h1>
            <table class="table table-striped">
                <thead>
                <tr>
                    <th></th>
                    <th>id</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                </tr>
                </thead>
                <?php

                $conn = mysqli_connect('db', 'root', 'test', "dbname");

                $query = 'SELECT * From Person';
                $result = mysqli_query($conn, $query);
                $cont =1;

                while($value = $result->fetch_array(MYSQLI_ASSOC)){
                    echo '<tr>';
                    echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
                    foreach($value as $element){
                        echo '<td>' . $element . '</td>';
                    }
                    $cont = $cont +1;
                    echo '</tr>';
                }

                $result->close();
                mysqli_close($conn);
                ?>
            </table>
        </div>

        <div class="row">
            <form id="form1">
              <div class="mb-3">
                <label class="form-label">Nombre</label>
                <input type="text" id="nom" class="form-control" name="nombre">
              </div>
              <div class="mb-3">
                <label class="form-label">Apellido</label>
                <input type="test" id="ape" class="form-control" name="apellido">
              </div>
              <button type="button" onclick="AgregarTabla()" class="btn btn-primary">Agregar</button>
            </form>
        </div>
    </div>
<script>
    function AgregarTabla() {
        var Nombre = document.getElementById("nom").value;
        var ape = document.getElementById("ape").value;
        var table = document.getElementById("tabla1");
        var tam = table.rows.length;
        var row = table.insertRow(tam);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = tam+"";
        cell2.innerHTML = Nombre;
        cell3.innerHTML = ape;
    }
</script>
</body>
</html>