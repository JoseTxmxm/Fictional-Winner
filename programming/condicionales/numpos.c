//Las condicionales if, else if nos permite que nuestro codigo se proceda si o no de 2 funciones especificadas en la escritura de este

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Promp user for num
float num = get_float("ingrese su numero: ");

// Num selection
if (num > 0)

printf("El numero es positivo\n");

else if (num < 0)

printf("El numero es negativo\n");

  return 0;
}
