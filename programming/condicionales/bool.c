//Escribir un codigo que verifique con valores booleanos int - char si un numero es divisible entre 2, si se trata de un numero par o impar

#include <cs50.h>
#include <stdio.h>

int main(void)
{
//Los resultados con decimales o fracciones corrsponde a numeros impares
//Los resultados con numeros enteros divisibles entre 2 corresponde a numeros pares
int num = get_int("Escriba aqui el numero: ");

if(num % 2 == 0)
printf("El numero %i es par\n", num);

else
printf("El numero %i es impar\n", num);

return 0;
}
