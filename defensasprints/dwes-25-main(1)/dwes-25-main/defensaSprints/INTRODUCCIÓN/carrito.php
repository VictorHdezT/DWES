<html>
  <body>
    <h1>Carrito</h1>
  <?php
$carrito = [
    "Manzana" => 0.5,
    "Pan" => 1.2,
    "Leche" => 0.9
];

$total = 0;
echo "<table border='1'><tr><th>Producto</th><th>Precio (€)</th></tr>";

foreach ($carrito as $producto => $precio) {
    echo "<tr><td>$producto</td><td>" . number_format($precio, 2) . "€</td></tr>";
    $total += $precio;
}

echo "<tr><td><b>TOTAL</b></td><td><b>" . number_format($total, 2) . "€</b></td></tr>";
echo "</table>";
?>
  </body>
</html>