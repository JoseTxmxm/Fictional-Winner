#include <stdio.h>
#include <stdlib.h>

#define N 10

int
main(int argc, char *argv[])
{
    //Must coment out of version 1 or version 2

    // Version 1 (bracket-type array)
    //int x[N];

    // Version 1 (pointer-type array)
    int *x = malloc(sizeof(int) * N);

    for (int i = 0; i < N; i++)
    {
        x[i] = i * 2;
    }

    for (int i = 0; i < N; i++)
    {
        printf("Element %d: %d\n", i, x[i]);
    }
}
