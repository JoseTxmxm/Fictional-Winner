#include <stdio.h>

//declarar la fucion o el procedimiento
int get_int();

//implementacion del procedimiento o la funcion
int get_int(int a, int b)//positivo = a, pos = b;
{
    int aux;
    aux = 0;

    do
    {
        printf("Ingrese un numero positivo:\n\n");
        scanf("%i", &a);
    }

    while (a < b);
    printf("En numero %i es positivo. Gracias!\n", a);

    return aux;
}

//llamar a la funcion
int main(int argc, char* argv[])
{
    int positivo, pos;
    positivo = 1;
    pos = 0;

    pos = get_int(positivo, pos);

    return 0;

}
