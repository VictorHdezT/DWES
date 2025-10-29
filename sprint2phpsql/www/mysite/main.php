<?php
// main.php — Listado de elementos con conexión a la base de datos

$dbHost = '127.0.0.1';
$dbName = 'mysitedb';
$dbUser = 'victor';   
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


$tables = ['tLibros', 'tJuegos']; 

function fetchAllFrom(PDO $pdo, $table) {
    $stmt = $pdo->prepare("SELECT * FROM `$table`");
    $stmt->execute();
    return $stmt->fetchAll();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Mi Site</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header>
  <h1>Listado de elementos — Mi Site</h1>
</header>

<main class="grid">
<?php foreach ($tables as $table): 
    $rows = fetchAllFrom($pdo, $table);
    if (count($rows) === 0) continue;
?>
  <section class="card">
    <h2><?php echo htmlspecialchars($table); ?></h2>
    <div class="items">
      <?php foreach ($rows as $row):
          $id = $row['id'] ?? null;
          $img = $row['imagen'] ?? $row['image'] ?? null;
      ?>
        <article class="item">
          <a class="item-link" href="detail.php?id=<?php echo urlencode($id); ?>">
            <div class="thumb">
              <?php if ($img): ?>
                <img src="<?php echo htmlspecialchars($img); ?>" alt="imagen">
              <?php else: ?>
                <div class="noimg">Sin imagen</div>
              <?php endif; ?>
            </div>
            <div class="meta">
              <?php foreach ($row as $col => $val): ?>
                <p><strong><?php echo htmlspecialchars($col); ?>:</strong> <?php echo htmlspecialchars($val); ?></p>
              <?php endforeach; ?>
            </div>
          </a>
        </article>
      <?php endforeach; ?>
    </div>
  </section>
<?php endforeach; ?>
</main>
</body>
</html>
