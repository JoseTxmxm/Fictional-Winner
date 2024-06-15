//Exploracion del uso, declaracion y definicion de las funciones

#include <stdio.h>

int maximo ();//Declaracion de la funcion maximo


int main()//Declaracion de main

{

    int x, y;

    x = 3;
    y = 10;

    maximo (x, y);//llamada

    printf("El valor de x en main es %i y el valor de y en main es %i.\n", x, y);

    return 0;
}

int maximo (int a, int b)//a = x ; b =y;
//Definicion de la funcion maximo
{
    a = 8;
    b = 5;
    printf("El valor de x en maximo es %i y el valor de y en maximo es %i.\n", a, b);
    return 0;
}
