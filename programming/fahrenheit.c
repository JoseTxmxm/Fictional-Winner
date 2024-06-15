//Escribir un codigo que convierta los grados celciiusC en grados fahrenheitF
//Los operadores aritmeticos nos facilitan los calculos para realizar diferentes funciones en nuestros programas

#include <cs50.h>
#include <stdio.h>

int main(void)
{

    float celsius, fahrenheit;

    printf("Ingrese los grados celsius:");
    scanf("%f",&celsius);

    fahrenheit = celsius * 9 / 5 + 32;

    printf("\nEl equivalente a grados fahrenheit son: %.2f\n", fahrenheit);


    return 0;
}

