<?php

include "connexion.php";

//recupere les articles de la base de donnée
$pdoStat = $pdo->prepare("SELECT * FROM article ");
$execute = $pdoStat->execute();
$articles = $pdoStat->fetchAll();

