
<html>
    <head>
        <title>Aplicaciones de Internet</title>
        <meta charset="utf-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    </head>
    <body>
    <?php
    $id =0;
    $nombre = "";
    $ape ="";
    //Comprobamos si los datos no vienen vacios.
    if(isset($_POST['num']) and isset($_POST['name']) and isset($_POST['ape'])){
            $id = (int) $_POST['num'];
            $nombre = $_POST['name'];
            $ape = $_POST['ape'];
            //echo "$id , $nombre ,$ape";
            $conn = mysqli_connect('db', 'root', 'test', 'dbname');

            if (!$conn) {
                die('Error de conexión: ' . mysqli_connect_error());
            }

            // Preparar la consulta SQL para insertar los datos en la tabla
            $query = "INSERT INTO Person (id,name, Apellido) VALUES ('$id','$nombre', '$ape')";

            // Ejecutar la consulta
            if (mysqli_query($conn, $query)) {
                echo "Datos guardados correctamente.";
            } else {
                echo "Error al guardar los datos: " . mysqli_error($conn);
            }

            // Cerrar la conexión
            mysqli_close($conn);

        }
    ?>
        <div class="container-fluid">
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
            <form action="/index.php" method="post">
                <div class="form-group">
                    <label for="name">nombre</label>
                    <input type="text" class="form-control" placeholder="Ingresa tu Nombre" id="name" name="name">
                </div>
                <div class="form-group">
                    <label for="ape">apellido</label>
                    <input type="text" class="form-control" placeholder="Ingresa tu Apellido" id="ape" name="ape">
                </div>
                <input type="hidden" id="num" name="num" value="<?php echo $cont; ?>" >
                <button type="submit" class="btn btn-primary">Ingresar</button>
            </form>
        </div>
    </body>
</html>
