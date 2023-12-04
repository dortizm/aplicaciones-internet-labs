<?php
// Conectarse a la base de datos
$conexion = mysqli_connect("db", "root", "test", "dbname");

// Validar los datos del formulario
if (empty($_POST["Nombre"]) || empty($_POST["Apellido"])) {
  echo "Por favor, complete todos los campos.";
  exit();
}

// Insertar los datos en la base de datos
$Nombre = $_POST["Nombre"];
$Apellido = $_POST["Apellido"];

$consulta = "INSERT INTO BaseDeDatos (Nombre, Apellido) VALUES ('$Nombre', '$Apellido')";
mysqli_query($conexion, $consulta);

// Redireccionar al usuario a la página principal
header("Location: codigoHtml.php");
?>
