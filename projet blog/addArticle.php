<?php

include "connexion.php";



$pdoStat=$pdo->prepare("INSERT INTO article VALUES (NULL, :titre, :description_courte, :description_longue)");



$titre = $_POST['titre'];
$description_courte = $_POST['description_courte'];
$description_longue = $_POST['description_longue'];



$pdoStat->bindValue(':titre', $titre, PDO::PARAM_STR);
$pdoStat->bindValue(':description_courte', $description_courte, PDO::PARAM_STR);
$pdoStat->bindValue(':description_longue', $description_longue, PDO::PARAM_STR);

$pdoStat->execute();






header("location: /ajoutearticles.php");
