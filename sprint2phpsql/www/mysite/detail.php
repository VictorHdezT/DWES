<?php
$dbHost = '127.0.0.1';
$dbName = 'mysitedb';
$dbUser = 'root';
$dbPass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$dbHost;dbname=$dbName;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $dbUser, $dbPass, $options);
} catch (PDOException $e) {
    die("Error de conexión: " . htmlspecialchars($e->getMessage()));
}

$id = intval($_GET['id'] ?? 0);

$stmt = $pdo->prepare("SELECT * FROM tJuegos WHERE id = ?");
$stmt->execute([$id]);
$juego = $stmt->fetch();
if (!$juego) die("Juego no encontrado");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuario_id = intval($_POST['usuario_id']);
    $comentario = trim($_POST['comentario']);
    if ($usuario_id && $comentario) {
        $stmt = $pdo->prepare("INSERT INTO tComentarios (comentario, usuario_id, juego_id) VALUES (?, ?, ?)");
        $stmt->execute([$comentario, $usuario_id, $id]);
        header("Location: detail.php?id=$id");
        exit;
    }
}

$stmt = $pdo->prepare("SELECT c.comentario, u.nombre, u.apellidos 
                       FROM tComentarios c
                       LEFT JOIN tUsuarios u ON c.usuario_id = u.id
                       WHERE c.juego_id = ?
                       ORDER BY c.id DESC");
$stmt->execute([$id]);
$comentarios = $stmt->fetchAll();

$usuarios = $pdo->query("SELECT * FROM tUsuarios")->fetchAll();
?>
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Detalle del Juego</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<h1><?php echo htmlspecialchars($juego['nombre']); ?></h1>

<section class="card">
  <?php if (!empty($juego['url_imagen'])): ?>
    <img src="<?php echo htmlspecialchars($juego['url_imagen']); ?>" alt="imagen" style="max-width:200px;">
  <?php endif; ?>
  <?php foreach ($juego as $col => $val): ?>
    <p><strong><?php echo htmlspecialchars($col); ?>:</strong> <?php echo htmlspecialchars($val); ?></p>
  <?php endforeach; ?>
</section>

<section class="card">
  <h2>Comentarios</h2>
  <?php if (!$comentarios): ?>
    <p>No hay comentarios aún.</p>
  <?php else: ?>
    <ul>
      <?php foreach ($comentarios as $c): ?>
        <li>
          <strong><?php echo htmlspecialchars($c['nombre'] . ' ' . $c['apellidos']); ?></strong><br>
          <?php echo nl2br(htmlspecialchars($c['comentario'])); ?>
        </li>
      <?php endforeach; ?>
    </ul>
  <?php endif; ?>
</section>

<section class="card">
  <h3>Añadir comentario</h3>
  <form method="post">
    <label>Usuario:
      <select name="usuario_id" required>
        <option value="">Selecciona</option>
        <?php foreach ($usuarios as $u): ?>
          <option value="<?php echo $u['id']; ?>"><?php echo htmlspecialchars($u['nombre'] . ' ' . $u['apellidos']); ?></option>
        <?php endforeach; ?>
      </select>
    </label><br>
    <label>Comentario:<br><textarea name="comentario" required rows="4" cols="40"></textarea></label><br>
    <button type="submit">Enviar</button>
  </form>
</section>
</body>
</html>
