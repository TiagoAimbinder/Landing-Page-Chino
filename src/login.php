<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manual Instructivo</title>
    <!-- Boostrap icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css">
    <!-- Css -->
    <link rel="stylesheet" href="../styles/login/index.css">
</head>
<body>
    <form action="" method="" class="form">

        <div class="top">
            <img src="../assets/Logo Picante.png" alt="Logo" class="img-logo">
            <div class="separator"></div>
        </div>

        <div class="container">
            <div class="group">
                <input type="text" name="user" class="input" placeholder=" " required>
                <label for="user" name="user" class="label">Nombre de usuario</label>
                <span class="line"></span>
            </div>
            <div class="group">
                <input type="password" name="pass" class="input" placeholder=" " required>
                <label for="pass" name="pass" class="label">Contraseña</label>
                <span class="line"></span>
            </div>
            
            <input type="submit" value="Iniciar Sesión" class="btn-submit">
            
        </div>
    </form>
    
</body>
</html>