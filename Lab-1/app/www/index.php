<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["nombre"];
    $last_name = $_POST["apellido"];
    if (empty($name) || empty($last_name)) {
        echo "Faltan datos";
    } else {
        $conn = mysqli_connect('db', 'root', 'test', 'dbname');
        if (!$conn) {
            die("Error al conectar a la base de datos: " . mysqli_connect_error());
        }
        $query_id = 'SELECT MAX(id) AS id FROM Names;';
        $result = mysqli_query($conn, $query_id);
        if ($result) {
            $id = ($result->fetch_object()->id) + 1;
            $query = "INSERT INTO Names VALUES (?, ?, ?)";
            $stmt = mysqli_prepare($conn, $query);
            mysqli_stmt_bind_param($stmt, 'iss', $id, $name, $last_name);
            
            if (mysqli_stmt_execute($stmt)) {
                echo "Registro agregado correctamente";
            } else {
                echo "Error al agregar el registro: " . mysqli_error($conn);
            }
            
            mysqli_stmt_close($stmt);
        } else {
            echo "Error al obtener el ID máximo: " . mysqli_error($conn);
        }

        mysqli_close($conn);
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Aplicaciones de Internet</title>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <div class="row">
            <h1>Aplicaciones de Internet</h1>
            <table class="table table-striped">
                <thead>
                <th></th>
                            <th>id</th>
                            <th>Nombre</th>
                            <th>Apellido</th>
                        </tr>
                    </thead>
                    <?php

                        $conn = mysqli_connect('db', 'root', 'test', "dbname");

                        $query = 'SELECT * From Names';
                        $result = mysqli_query($conn, $query);

                        while($value = $result->fetch_array(MYSQLI_ASSOC)){
                            echo '<tr>';
                            echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
                            foreach($value as $element){
                                echo '<td>' . $element . '</td>';
                            }

                            echo '</tr>';
                        }

                        $result->close();
                        mysqli_close($conn);
                    ?>
                    </table>
            </div>
        </div>
        <div class="row">
            <form method="POST" action="index.php">
                <div class="mb-3">
                    <label class="form-label">Nombre</label>
                    <input type="text" class="form-control" name="nombre">
                </div>
                <div class="mb-3">
                    <label class="form-label">Apellido</label>
                    <input type="text" class="form-control" name="apellido">
                </div>
                <button type="submit" class="btn btn-primary">Agregar</button>
            </form>
</body>
</html>
