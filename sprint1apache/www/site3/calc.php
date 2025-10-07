<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $n1 = $_POST["n1"];
    $n2 = $_POST["n2"];
    $op = $_POST["op"];
    $resultado = 0;

    switch ($op) {
        case "suma": $resultado = $n1 + $n2; break;
        case "resta": $resultado = $n1 - $n2; break;
        case "multiplicacion": $resultado = $n1 * $n2; break;
        case "division": $resultado = $n2 != 0 ? $n1 / $n2 : "Error (división por 0)"; break;
    }
    echo "$n1 $op $n2 = $resultado";
} else {
?>
<form method="post">
    <input type="number" name="n1" required>
    <select name="op">
        <option value="suma">+</option>
        <option value="resta">-</option>
        <option value="multiplicacion">*</option>
        <option value="division">/</option>
    </select>
    <input type="number" name="n2" required>
    <button type="submit">Calcular</button>
</form>
<?php } ?>
