<!DOCTYPE html>
<html lang="es">
<head>
  <title>Registro</title>
</head>
<body>
  <h1>Registro</h1>
  <form action="guardarDatos.php" method="post">
    <input type="text" name="Nombre" placeholder="Nombre">
    <input type="text" name="Apellido" placeholder="Apellido">
    <input type="submit" value="Enviar">
  </form>

  <h1>Aplicaciones de Internet Prueba</h1>
  <table class="table table-striped">
      <thead>
          <tr>
              <th></th>
              <th>Nombre</th>
              <th>Apellido</th>
          </tr>
      </thead>
      <?php

          $conn = mysqli_connect('db', 'root', 'test', "dbname");

          $query = 'SELECT * From BaseDeDatos';
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
</body>
</html>
