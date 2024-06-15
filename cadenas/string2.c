#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Escriba su cadena aqui:");

    if (s != NULL)//La implementacion de esta condicion se sersiora de que el programa ejecute cadenas que no esten ahi;
    {
    for (int i = 0; i < strlen(s); i++)
    {
        printf("%c\n", s[i]);
    }
    }
}
