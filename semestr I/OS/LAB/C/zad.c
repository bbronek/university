#include <stdio.h>
#include <ctype.h>

int main() {
    int c;
    FILE *FILE;
    char filel[20];
    scanf("%s", filel);


    FILE = fopen(filel, "rb");


    while ((c = fgetc(FILE)) != EOF)
    {
        if (!isascii(c)) 
        {
            printf("0");
            return 0;
        }
        
    }

    printf("1");
    return 0;

}