//Ejecutar ejemplos dentro de main y funcion maximo

#include <stdio.h>

//Declaracion de la funcion maximo
int maximo();

//Declaracion de main
int main()
{
    maximo();//llamada de la funcion maximo
    printf("Estamos dentro de main\n");
    return 0;
}

int maximo()//Definicion de la funcion maximo
{
    printf("La funcion de maximo ha sido definida\n");
    return 0;
}
