//Escribir un codigo que asigne un voto a una edecan dependiendo del numero elegido
//El condicional switch nos sirve para elegir entre distintas funciones creadas en lenguajes de programacion

#include <cs50.h>
#include <stdio.h>

int main(void)

{
  int edecan = get_int("Ingrese su numero de la edecan del 1-5:");

switch(edecan){

    case 1: printf("Usted a votado por Noelia\n");
    break;
    case 2: printf("Usted a votado por Florencia\n");
    break;
    case 3: printf("Usted a votado por Mariana\n");
    break;
    case 4: printf("Usted a votado por viridiana\n");
    break;
    case 5: printf("Usted a votado por Angelica\n");
    break;
    default: printf("Usted no a votado por ninguna de nuestras edecanes\n");}

}





