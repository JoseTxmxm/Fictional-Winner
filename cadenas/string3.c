//Mejora del programa que aumenta la eficiencia y reduce la repeticion inecesarias
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Ingrese su cadena aqui:");

    if (s != NULL)
    {
        for (int i = 0, n = strlen(s); i < n; i++)//Declarando la variable n = strlen para la incializacion del calculo de la cadena se evita repeticiones inecesarias
        {
            printf("%c\n", s[i]);
        }
    }
}
