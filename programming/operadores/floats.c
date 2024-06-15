//Los operadores nos no diferencian mucho de los operadores matematicos y se utilizan para realizar operaciones aritmeticas en un lenguaje de programacion

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Promt user for x
    float x = get_float("x: ");

    //Promt user for y
    float y = get_float("y: ");

    //Perform arithmetic
    printf("%f plus %f is %f\n", x, y, x + y);
    printf("%f minus %f is %f\n", x, y, x - y);
    printf("%f times %f is %f\n", x, y, x * y);
    printf("%f diveded by %f is %f\n", x, y, x / y);
    printf("remainder of %f divided by %f is %f\n", x, y, x / y);
}
