#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(int argc, char** argv)
{
 printf( "----------------------plus ou moins---------------------------\n\n\n");
 
 srand(time(NULL));
 int nombreDECoup =0;
 int nombreEntre =0;
 int nombreMystere=0;
 const int MIN = 0;
 int niveau = 0;
 int compteur = 0;
 int tpsrest = 0;
 int modeJoueur;
int nombreMaximum=0
// en haut se sont les renitialisations des variables et les declarations de variable.
 
 
 
 
 
 
 
 
 
 
 
 
 
{ printf("choisissez votre mode de joueur\n");/* le chois des mode dans un menus
                                          mais a cette ligne on m'affiche une belle erreur au lieu d'un programme magnifique
                                            aidez moi s'il vous plait.
                                               */
 
 
 
 printf("1 modeJoueur1\n");
 printf("2 modeJoueur2\n");
 scanf("%d", &modeJoueur);                  // le choix des niveaux dans un menus donc cela fait un double menus
if (modeJoueur == 1)
 
  printf("quel est le niveau de difficultes voulez vous");
  printf("1 facile(entre 1 a 100)\n");
  print("2 difficile(entre 1 a 1000\n");
  printf("impossible (entre 1 a 10000 en moins de 25 coups\n)");
  scanf("%d",&niveau);
  if (niveau = 1)
 
   nombreMaximum = 100;
   nombreMystere = (rand() % (nbMax - MIN + 1)) + MIN; // generations du nombreMystere generer par la machine.
 while(nombreMystere != nombreEntre)
 {
 
      printf("quel est le nombre mystere\n"); // demande de trouver mantenant le nombreMystere
      scanf("%d", &nombreEntre);
      if(nombreEntre > nombreMystere)
    {
      printf("c'est c'est moins\n");
    }
      else if (nombreEntre < nombreMystere)
    {
      printf("c'est plus\n");
    }
      else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur);// ici la compilations du compteur c'est a dire le compteur de coup
      compteur++
    }
      else if (niveau = 2)// et ainsi de suit presque la meme chose
 
     nombreMaximum = 1000;
     nombreMystere = (rand() % (nbMax - MIN + 1)) + MIN;
     while(nombreMystere != nombreEntre)
    {
      printf("quel est le nombre mystere\n");
      scanf("%d", &nombreEntre);
      if(nombreEntre > nombreMystere)
    {
      printf("c'est c'est moins\n");
    }
     else if (nombreEntre < nombreMystere)
    {
      printf("c'est plus\n");
    }
    else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur)
      compteur++
    }
 
   if ( niveau == 3)
      nombreMaximum = 10000;
     nombreMystere = (rand() % (nbMax - MIN + 1)) + MIN;
     while(nombreMystere != nombreEntre)
    {
      printf("quel est le nombre mystere\n");
      scanf("%d", &nombreEntre);wxcf("c'est plus\n");
    }
    else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur)
      compteur++
    }
  } else if(modeJoueur == 2)
  printf("choisisser votre niveau de difficulte\\n\n\n");// ici c'est le mode joueur de la il faut jouer avec deux joueurs
  printf("1 facile");
  printf("2 difficile");
  printf("3 impossible");
  scanf("%d", &niveau);
  if (niveau==1)
  printf("entrer un nombre de 1 a 100");
  scanf("%d", nombreEntre);
 
    while(nombreMystere != nombreEntre)
    {
      printf("quel est le nombre mystere\n");
      scanf("%d", &nombreEntre);
      if(nombreEntre > nombreMystere)
    {
      printf("c'est c'est moins\n");
    }
     else if (nombreEntre < nombreMystere)
    {
      printf("c'est plus\n");
    }
    else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur)
      compteur++
    }
    else if (niveau == 2)
 
 printf("entrer un nombre de 1 a 1000");
  scanf("%d", nombreEntre);
 
    while(nombreMystere != nombreEntre)
    {
      printf("quel est le nombre mystere\n");
      scanf("%d", &nombreEntre);
      if(nombreEntre > nombreMystere)
    {
      printf("c'est c'est moins\n");
    }
     else if (nombreEntre < nombreMystere)
    {
      printf("c'est plus\n");
    }
    else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur)
      compteur++
     }
 
  else if (niveau == 3)
 
 printf("entrer un nombre de 1 a 10000");
  scanf("%d", nombreEntre);
 
    while(nombreMystere != nombreEntre)
    {
      printf("quel est le nombre mystere\n");
      scanf("%d", &nombreEntre);
      if(nombreEntre > nombreMystere)
    {
      printf("c'est c'est moins\n");
    }
     else if (nombreEntre < nombreMystere)
    {
      printf("c'est plus\n");
    }
    else
    {
      printf("BRAVO! vous avez trouvez le nombre mystere en %d coups\n\n", compteur)
      compteur++
    }
 
 
 
 
 
 
 
 
    return 0;
}