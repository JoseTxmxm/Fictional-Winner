#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
    //our program goes here
    for (int i = 0; i < argc; i++)
        printf("argv[%d] is: %s\n", i, argv[i]);

}
