//Los operadores aritmeticos nos facilitan los calculos para realizar diferentes funciones en nuestros programas

#include <cs50.h>
#include <stdio.h>

int main(void)
{

    //Promt user for fahrenheit
    float fahrenheit;

    //Prompt user for celsius
    float celsius = get_float("Igrese los grados celsius: ");

    //Perform arithmetic
    fahrenheit = (celsius * 9 / 5) + 32;
    printf("\nEl equivalente de %.2f grados celsius es de %.2f grados fahrenheit\n", celsius, fahrenheit);

    return 0;
}
