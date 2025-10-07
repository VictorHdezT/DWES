<?php
function calcular_imc($peso, $altura) {
    return $peso / ($altura * $altura);
}

$peso = $_GET['peso'] ?? null;
$altura = $_GET['altura'] ?? null;

if ($peso && $altura) {
    $imc = calcular_imc($peso, $altura);
    echo "Tu IMC es: " . round($imc, 2) . "<br>";

    if ($imc < 18.5) {
        echo "Bajo peso";
    } elseif ($imc < 25) {
        echo "Normal";
    } else {
        echo "Sobrepeso";
    }
} else {
    echo "Por favor, indica peso y altura (ejemplo: ?peso=70&altura=1.75)";
}
?>
