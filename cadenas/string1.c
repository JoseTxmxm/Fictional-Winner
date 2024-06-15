#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Escriba su cadena aqui:");

    for (int i = 0; i < strlen(s); i++)//strlen calcula el largo de una cadena string
    {
        printf("%c\n", s[i]);
    }
}
