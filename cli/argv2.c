#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    //our program goes here
    for (int i = 0; i < argc; i++)
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        printf("argv[%d][%d] is: %c\n", i, j, argv[i][j]);
}
