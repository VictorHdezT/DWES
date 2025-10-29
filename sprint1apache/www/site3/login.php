<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST["usuario"];
    $pass = $_POST["password"];

    if ($user === "admin" && $pass === "1234") {
        echo "Acceso concedido";
    } else {
        echo "Acceso denegado";
    }
} else {
?>
<form method="post">
    Usuario: <input type="text" name="usuario" required><br>
    Contraseña: <input type="password" name="password" required><br>
    <button type="submit">Entrar</button>
</form>
<?php } ?>
