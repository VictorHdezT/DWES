
<html>
  <body>
    <h1>Conversión de temperaturas</h1>
    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $cantidad = $_POST["cantidad"];
    $tipo = $_POST["tipo"];

    if ($tipo == "cf") {
        $resultado = ($cantidad * 9/5) + 32;
        echo "$cantidad ºC = " . round($resultado, 2) . " ºF";
    } else {
        $resultado = ($cantidad - 32) * 5/9;
        echo "$cantidad ºF = " . round($resultado, 2) . " ºC";
    }
} else {
?>
<form method="post">
    <input type="number" step="any" name="cantidad" required>
    <label><input type="radio" name="tipo" value="cf" checked> Celsius → Fahrenheit</label>
    <label><input type="radio" name="tipo" value="fc"> Fahrenheit → Celsius</label>
    <button type="submit">Convertir</button>
</form>
<?php } ?>
  </body>
</html>