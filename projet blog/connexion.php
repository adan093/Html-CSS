<?php

try {

// Sous MAMP (Mac)
$pdo = new PDO('mysql:host=localhost;dbname=espace_membre;charset=utf8', 'root', 'root');
// Gestion des erreurs
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	echo "vous etes bien connecté à la base de donnée | \n";

} catch (PDOException $pika ) {

// afficher de l'erreur si mauvaise connection
	echo $pika->getMessage();
	// arrete la connexion
	die;


}
//------------------------------------------------------------------------ -//>
