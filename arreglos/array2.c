#include <stdio.h>
#include <stdlib.h>

#define N 10

int main(int argc, char *argv[])
{
    //Must coment out of version 1 or version 2

    // Version 1 (bracket-type array)
    //int x[N];

    // Version 1 (pointer-type array)
    //int *x = malloc(sizeof(int) * N);

int x[] = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18};//Con la declaracion del [arreglo tipo puntero] no es posible delacaralo de esta manera; [arreglo tipo soporte]
  for (int i = 0; i < N; i++)

{
      printf("Element %d: %d\n", i, x[i]);
}
}
