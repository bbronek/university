#include <unistd.h>
#include <iostream>
#include<stdio.h> //printf
#include<string.h> //memset
#include<stdlib.h> //exit(0);
#include<arpa/inet.h>
#include<sys/socket.h>

#define BUFLEN 512  //Max length of buffer


using namespace std;

void die(char *s)
{
        perror(s);
        exit(1);
}

int main(void)
{
        char adres[512];
        struct sockaddr_in si_other;
        int s, i, portno;
	socklen_t slen=sizeof(si_other);
        char buf[BUFLEN];
        char message[BUFLEN];

        printf("IP: ");
        scanf("%s", adres);
        printf("Port: ");
        scanf("%u", &portno);

        if ( (s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
        {
                die("socket");
        }

        memset((char *) &si_other, 0, sizeof(si_other));
        si_other.sin_family = AF_INET;
        si_other.sin_port = htons(portno);

        if (inet_aton(adres , &si_other.sin_addr) == 0)
        {
                fprintf(stderr, "inet_aton() failed\n");
                exit(1);
        }

        while(1)
        {
                printf("Enter message : ");
                scanf("%s", message);

                //send the message
                if (sendto(s, message, strlen(message) , 0 , (struct sockaddr *) &si_other, slen)==-1)
                {
                        die("sendto()");
                }

                //receive a reply and print it
                //clear the buffer by filling null, it might have previously received data
                memset(buf,'\0', BUFLEN);
                //try to receive some data, this is a blocking call
                if (recvfrom(s, buf, BUFLEN, 0, (struct sockaddr *) &si_other, &slen) == -1)
                {
                        die("recvfrom()");
                }

                puts(buf);
        }

        close(s);
        return 0;
}
