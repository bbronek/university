//Bartosz Bronikowski Microshell 2021
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <dirent.h>
#include <sys/types.h>
#include <fcntl.h>
#include <time.h>
#include <limits.h>
#include <stdbool.h> 
#include <regex.h>
#include <signal.h>

#define MAGENTA(string) "\x1b[35m" string "\x1b[0m"
#define CYAN(string)    "\x1b[36m" string "\x1b[0m"
#define GREEN(string)   "\x1b[32m" string "\x1b[0m"
#define YELLOW(string)  "\x1b[33m" string "\x1b[0m"
#define RED(string)     "\x1b[31m" string "\x1b[0m"
#define TRUE 1
#define BUFFER_SIZE 4096
#define MAX_MATCHES 1


char cmd[1024];
int historyCount = 0;
char *history[2048];
char varx[12][12];
int vargc = 1;
int l = 0 , k = 0;
int b = -1,e=-1;
void swap(int *x, int *y) 
{ 
    int temp = *x; 
    *x = *y; 
    *y = temp; 
}
void signal_handler(int signal)
{
    printf("Error: stop is nor allowed");
}

void regex_match(regex_t *data, char *pattern)
{
    regmatch_t matches[MAX_MATCHES];
    if(regexec(data,pattern,MAX_MATCHES,matches,0) == 0)
    {
        b = matches[0].rm_so;
        e = matches[0].rm_eo;
    }
}

int grep_impl(char *params[])
{
    

    if(vargc <3)
    {
        printf("Too less arguments , please add file address or eventually flags");
        return 0;
    }

    if(vargc >3)
    {
        puts("Too many argumnets if you don't know how to use this command check it out at help");
        return 0;
    }
    int ret;
    regex_t rex;
    ret = regcomp(&rex,params[1],REG_EXTENDED);
    if(ret != 0)
    {
        printf("Regular expressions failed , error code:%d",ret);
    }
    

    char word[1024];
    FILE *file;
    file = fopen(params[2],"r");
    if(file != NULL)
    {
        while (fscanf(file,"%s",word)!=EOF)
        {
            b=-1;
            e=-1;
            regex_match(&rex,word);
            if(b!=-1)
            {
                for(int i=0;i<strlen(word);++i)
                {
                    if(b==i)
                    {
                        for(int i = b;i<e;++i)
                            printf(RED("%c"),word[i]);
                        i = e;
                    }
                    printf("%c",word[i]);
                    regex_match(&rex,word);
                }
                printf("\n");
            }
        }

    fclose(file);

    
    }

    if(file ==NULL )
    {
        printf("Can not open a file please check file name");
    }
    return 0;
}

void sort_words_alpha(char *words[],int indexes[],int size)
{
    char *pom;
    for(int i =0;i<size;++i)
    {
        for(int j = i+1;j<size;++j)
        {
            if(strcmp(words[i],words[j]) > 0)
            {
                
                
                swap(&indexes[i],&indexes[j]);
                pom = words[j];
                words[j] = words[i];
                words[i] = pom;
            }
        }
    }

}

void sort_words_beta(char *words[],int indexes[],int size)
{
    char *pom;
    for(int i =0;i<size;++i)
    {
        for(int j = i+1;j<size;++j)
        {
            if(strcmp(words[i],words[j]) < 0)
            {
                
                
                swap(&indexes[i],&indexes[j]);
                pom = words[j];
                words[j] = words[i];
                words[i] = pom;
            }
        }
    }

}


void sort_nflag(char *words[],int indexes[],int size)
{
    char *pom;
    for(int i =0;i<size;++i)
    {
        for(int j = i+1;j<size;++j)
        {
            if((atoi(words[i]))>(atoi(words[j])))
            {
                
                
                swap(&indexes[i],&indexes[j]);
                pom = words[j];
                words[j] = words[i];
                words[i] = pom;
            }
        }
    }

}
time_t t;
void sort_random(char *words[],int indexes[],int size)
{
    char *pom;
    for(int i =0;i<size;++i)
    {
        for(int j = i+1;j<size;++j)
        {
                swap(&indexes[rand()%size],&indexes[rand()%size]);
                pom = words[j];
                words[j] = words[i];
                words[i] = pom;
        }
    }

}

void cp_to_file(char *words[], int size,char *to)
{

    FILE* file = fopen(to,"w");
    for(int i=0;i<size;++i)
    {
       
        fputs(words[i],file);
    }

    fclose(file);

    
}

int indexes[2048];
int sort_impl(char *params[])
{

    if(vargc ==1)
    {
        printf("Too less arguments , please add file address or eventually flags");
        return 0;
    }

    if(vargc >5)
    {
        puts("Too many argumnets if you don't know how to use this command check it out in help");
        return 0;
    }
    int size = 0;
    char word[256],*wufsort[2048],*lines[2048];
    FILE *file;
    size_t len = 0;
    ssize_t readLine;
    file = fopen(params[1],"r");
    
    if(file != NULL)
    {
        while (fscanf(file,"%s%*[^\n]",word)!=EOF)
        {
            wufsort[size] = malloc(1000);
            strcpy(wufsort[size],word);
            indexes[size] = size;
            ++size;
        }
        fclose(file);
        file = fopen(params[1],"r");
        size = 0;
        while ((readLine = (getline(&lines[size],&len,file))) != -1)
        {
            ++size;
        }


    fclose(file);

    }

    else
    {
        printf("Something went wrong.You don't have permission to a file or it doesn't exist.");
        return 0;
    }

    if(vargc==2)
    {
        sort_words_alpha(wufsort,indexes,size);

        for(int i =0;i<size;++i)
        {
            printf("%s",lines[indexes[i]]);
        }

        return 0;
    }

    if((vargc == 3) && ((strcmp(params[1],"-r")==0) || ((strcmp(params[2],"-r")==0))))
    {
        sort_words_alpha(wufsort,indexes,size);

        for(int i =(size-1);i>=0;i--)
        {
            printf("%s",lines[indexes[i]]);
        }

        return 0;
    }

    if((vargc == 3 )&& ((strcmp(params[1],"-n")==0) || ((strcmp(params[2],"-n")==0))))
    {
        sort_nflag(wufsort,indexes,size);

        for(int i =0;i<size;++i)
        {
            printf("%s",lines[indexes[i]]);
        }
      

        return 0;
    }

    if((vargc == 3) && ((strcmp(params[1],"-R")==0) ||((strcmp(params[2],"-R"))==0)))
    {
        sort_random(wufsort,indexes,size);

        for(int i =0;i<size;++i)
        {
            printf("%s",lines[indexes[i]]);
        }
      

        return 0;
    }

    if(vargc == 4 && strcmp(params[2],">")==0)
    {
        sort_words_alpha(wufsort,indexes,size);
        cp_to_file(lines,size,varx[3]);
        return 0;
    }
    if(vargc == 5 && strcmp(params[3],">")==0)
    {
        
        if((strcmp(params[1],"-r")==0) || (strcmp(params[2],"-r")==0))
            {
                sort_words_beta(wufsort,indexes,size);
            }

        if((strcmp(params[1],"-n")==0) || (strcmp(params[2],"-n")==0))
        {
            sort_nflag(wufsort,indexes,size);

        }

        if((strcmp(params[1],"-R")==0) || (strcmp(params[2],"-R")==0))
        {
            
            sort_random(wufsort,indexes,size);
        }


        cp_to_file(wufsort,size,varx[4]);
        return 0;
    }
    
    

    else
    {
        printf("Something went wrong , use help if you don't know how to use this command.");
        return 0;
    }


    
}

void type_prompt() 
{ 
    char buff[1024]; 
    getcwd(buff, sizeof(buff)); 
    printf("\n""["MAGENTA("%s")":"CYAN("%s")"]\n$ ", getenv("USER"), buff); 
} 

void help()
{
    printf("\n"YELLOW("%s")GREEN("%s")YELLOW("%s")GREEN("%s")CYAN("%s"),
    "\t\t*** MICROSHELL PROJECT 2021 ***\n",
    "Author: Bartosz Bronikowski\n\n",
    "Commands implemented by me:\n\t\t1. cd - it works almost the same as bash version , cd [{path}] | cd .. | cd - | cd |cd~\n\t\t2. exit - this command ends working of program\n\t\t3. help - informations about author and features\n\t\t4. grep - grep [pattern] file.txt\n\t\t5. sort - sort file.txt | sort file.txt -r (sorting in reverse order) | sort file.txt -n (sort numbers) | sort file.txt -R (sort in random way) | sort file.txt -flag > file2.txt (flag is optional , copying results of sorting to new or existing file)\n",
    "Other commands are executed by fork() + exec*\n\n",
    "Bajery: colors,username,signals,arguments in qutation marks,\n");

}

void clear_input()
{
    for(int i=0;i<l+1;++i)
    {
        for(int j=0;j<k;++j)
        {
            varx[i][j] = '\0';
        }
    }
}
void input(char *params[])
{
    l = 0;
    k = 0;
    historyCount++;
    vargc = 1;
    fgets(cmd,1024,stdin);
    cmd[strlen(cmd)-1] = '\0';
    history[historyCount] = cmd;
   
    for(int i = 0;i<strlen(cmd);++i)
    {
        if(cmd[i]==' ' || cmd[i]=='\0' )
        {
            varx[l][k]='\0';
            ++l;
            k = 0;
            vargc++;
            continue;
        }

        if(cmd[i]=='\"')
        {
            continue;
        }
        
        else
        {
            varx[l][k] = cmd[i];
            k++;
            
        }
        
    }
    for(int i = 0;i<=l;++i)
    {
        params[i] = varx[i];
    }
    params[l+1] = NULL;
}


char *temp = NULL;
int cd()
{
    temp = getcwd(temp, PATH_MAX);
    static char prev[PATH_MAX];
    if (vargc>2) 
    {
        perror("too many arguments");
        return 0;
    }

    if (vargc == 1 || strcmp(varx[1],"~")==0)
    {
        char* HOME = getenv("HOME");
        chdir(HOME);
        return 0;
    }

    if (strcmp(varx[1],"-") == 0)
    {
        chdir(prev);
        return 0;
    }

    int r;
    strcpy(prev,temp);
    r = chdir(varx[1]);
    if(r==0) return 0;

    else printf("Something went wrong, error code %d , %s",errno,strerror(errno));
   
    
    return 0;
}

char *params[42] = {NULL};
int cmdx = 0;
int cmdy = 0;
int main(int argc, char *argv[])
{
    
    struct sigaction sa;
    sa.sa_handler = &signal_handler;

    while(TRUE)
    {
        srand((unsigned) time(&t));
        type_prompt();
        clear_input();
        input(params);
        sigaction(SIGCONT,&sa,NULL);

        

        if(strcmp(cmd,"exit") == 0)
        {
            return 0;
        }

        if(strcmp(cmd,"help") == 0)
        {
            help();
            continue;
        }

        if(strcmp(varx[0],"cd") == 0)
        {
        
            cd();
            continue;
        }

        if(strcmp(varx[0],"grep") == 0)
        {
            grep_impl(params);
            continue;
        }

        if(strcmp(varx[0],"sort") == 0)
        {
            sort_impl(params);
            continue;
        }


        else
        {
            
            pid_t id = fork();
            if (id ==-1) exit(1);
            if (id ==0) 
            {
        
                    execvp(varx[0],params);
                    fprintf(stderr,"Microshell command not found :%s. , error code:%d. %s",varx[0],errno,strerror(errno));
                    exit(0);
                
            }
            else if (id >0)
            {
                wait(NULL);
                
            }
            
        }     
        
    }
    
    return 0;
}