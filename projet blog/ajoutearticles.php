

	<!DOCTYPE HTML>

<html>
	<head>
		<title>MyBlogMusic</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="ajoute.css" />
	</head>


	<body>
		<?php include "showArticle.php"; ?>

		<?php foreach ($articles as $article): ?>

		<h1> <?= $article['titre'] ?> </h1>

		<?php endforeach; ?>

			<nav id="nav">
				<ul class="container">
					<li><a href="ajoutearticle">AJOUTER VOS ARTICLE</a></li>
				</ul>
			</nav>
			<br/><br/><br/><br/><br/>



	<div class="containerformulaire">
		<div class="formulaire">
			<h2> Veuillez remplir le formulaire suivant</h2>
			<form method="POST" action="addArticle.php">
				<label for="titre">Titre de l'article : </label> 
				<input type="text" name="titre" /> <br>

				<label for="description_longue">Description longue :</label> 
					<textarea name="description_longue" rows="10" maxlength="500"></textarea><br>
					

				<label for="description_courte"> Description courte :</label>
					<textarea name="description_courte" rows="10" maxlength="500"></textarea><br>
					

				


                    <input type="submit" name="Ajouter" value="Ajouter" />

			</form>

		</div>
		</div>


	

	</body>
</html>