#include <stdio.h>
#include <stdlib.h>

int main()
{
    int main()
{
float euro = 1,dollard = 1.5,yenJaponais = 150;


int Change(float nombre,int choix)
{
if(choix ==0) // si le choix est euro => dollars
{nombre *1.5 ;}
if(choix ==1) // si euro=> yen japonais
{nombre *150;}
 
// etc...
 
return nombre;
}

Change(50,1);

printf("%f",Change(50,1));

// ou comme ça

nombre = Change(50,1);
printf("%f",nombre);

}
}
