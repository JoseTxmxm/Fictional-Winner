//El bucle while realiza la automatizacion de la repeticion de la variable positivo hasta que se imprima la verificacion de un numero positivo
#include <cs50.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
    int positivo = 0;

do
{
    printf("Type a positive number:");
    scanf("%d", &positivo);
}

    while (positivo < 0);
   printf("Do you typed for a positive number, try again!\n");

   if (positivo < 0)
   printf("\n");

    return 0;
}
