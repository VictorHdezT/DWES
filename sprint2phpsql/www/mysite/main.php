<?php
$dbHost = '127.0.0.1';
$dbName = 'mysitedb';
$dbUser = 'root';
$dbPass = '1234';
$charset = 'utf8mb4';

$dsn = "mysql:host=$dbHost;dbname=$dbName;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $dbUser, $dbPass, $options);
} catch (PDOException $e) {
    http_response_code(500);
    echo "Error de conexión: " . htmlspecialchars($e->getMessage());
    exit;
}

// Obtener todos los juegos
$stmt = $pdo->query("SELECT * FROM tJuegos");
$juegos = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Listado de Juegos</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header>
  <h1>Listado de Juegos</h1>
</header>

<main class="grid">
  <?php foreach ($juegos as $juego): ?>
    <article class="item">
      <a href="detail.php?id=<?php echo $juego['id']; ?>">
        <div class="thumb">
          <?php if (!empty($juego['url_imagen'])): ?>
            <img src="<?php echo htmlspecialchars($juego['url_imagen']); ?>" alt="imagen">
          <?php else: ?>
            <div class="noimg">Sin imagen</div>
          <?php endif; ?>
        </div>
        <div class="meta">
          <?php foreach ($juego as $col => $val): ?>
            <p><strong><?php echo htmlspecialchars($col); ?>:</strong> <?php echo htmlspecialchars($val); ?></p>
          <?php endforeach; ?>
        </div>
      </a>
    </article>
  <?php endforeach; ?>
</main>
</body>
</html>

