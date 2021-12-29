#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#define BUFFER_SIZE 4028

char varx[12][12];
char *params[42] = {NULL};
int main(int argc, char *argv[])
{

    char buffer[BUFFER_SIZE];
    int num,fd;
    char *data = calloc(1,1);
    
    while ((num = read(STDIN_FILENO, &buffer, BUFFER_SIZE)) > 0)
    {
        data = realloc(data,strlen(data)+1+strlen(buffer));
        strcat(data,buffer);
    }
    int l = 0 , k =0 ;

    for(int i = 0;i<strlen(data);++i)
    {
        if(data[i]==' ' || data[i]=='\0' )
        {
            varx[l][k]='\0';
            ++l;
            k = 0;
        }
        else if (data[i]=='\n') continue;
        else
        {
            varx[l][k] = data[i];
            k++;
            
        }
        
    }
    for(int i = 0;i<=l;++i)
    {
        params[i] = varx[i];
    }
    
    char ch;
    FILE *file;
    file = fopen(params[0],"r");
    printf("%s",params[0]);
    if(file != NULL)
    {
        while (!feof(file))
        {
            ch = fgetc(file);
            if(isascii(ch) == 0)
            {
                printf("0");
                return 0;
            }
        }
    }
    printf("1");






return 0;
}