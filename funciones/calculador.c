//Calcular cual numero tiene el valor maximo por medio de una estructura de algoritmo que contenga la funcion

#include <stdio.h>

//Declaracion de la funcion maximo
int maximo();

int main()
{
    int x, y, max;

    x = 3;
    y = 10;

    max = maximo(x, y);//Llamado de la funcion
    printf("El valor maximo es %i.\n\n",max);

    return 0;
}

//Definicion de la funcion maximo
int maximo(int a, int b)//a =x; b = y;
{
    int aux;

    if(a > b)
    {
     aux = a;
    }
    else
    {
        aux = b;
    }
    return aux;
}
