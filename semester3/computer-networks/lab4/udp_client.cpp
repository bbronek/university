#include <unistd.h>
#include <iostream>
#include<stdio.h> //printf
#include<string.h> //memset
#include<stdlib.h> //exit(0);
#include<arpa/inet.h>
#include<sys/socket.h>

#define BUFLEN 512  //Max length of buffer


using namespace std;

void die(const char *s)
{
        perror(s);
        exit(1);
}

int main(void)
{
        char address[512];
        struct sockaddr_in si_other;
        int s, portno;
	socklen_t slen=sizeof(si_other);
        char buf[BUFLEN];
        char message[BUFLEN];

        printf("IP: ");
        if (scanf("%511s", address) != 1) return 1;
        printf("Port: ");
        if (scanf("%d", &portno) != 1 || portno < 1 || portno > 65535) return 1;

        if ( (s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
        {
                die("socket");
        }

        memset((char *) &si_other, 0, sizeof(si_other));
        si_other.sin_family = AF_INET;
        si_other.sin_port = htons(portno);

        if (inet_aton(address , &si_other.sin_addr) == 0)
        {
                fprintf(stderr, "inet_aton() failed\n");
                exit(1);
        }

        while(1)
        {
                printf("Enter message : ");
                if (scanf("%511s", message) != 1) break;

                //send the message
                if (sendto(s, message, strlen(message) , 0 , (struct sockaddr *) &si_other, slen)==-1)
                {
                        die("sendto()");
                }

                //receive a reply and print it
                //clear the buffer by filling null, it might have previously received data
                memset(buf,'\0', BUFLEN);
                //try to receive some data, this is a blocking call
                if (recvfrom(s, buf, BUFLEN - 1, 0, (struct sockaddr *) &si_other, &slen) == -1)
                {
                        die("recvfrom()");
                }

                puts(buf);
        }

        close(s);
        return 0;
}
