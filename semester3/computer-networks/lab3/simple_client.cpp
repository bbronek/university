#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>
#include <string.h>

int main(void) {
        char abcd[512];
        int sockfd, portno, n;
        struct sockaddr_in serv_addr = {};

        char buffer[256];

        printf("Enter the recipient IP address: ");
        if (scanf("%511s", abcd) != 1) return 1;
        printf("Enter the recipient port: ");
        if (scanf("%d", &portno) != 1 || portno < 1 || portno > 65535) return 1;

        /* Create a socket point */
        sockfd = socket(AF_INET, SOCK_STREAM, 0);

        if (sockfd < 0) {
                perror("ERROR opening socket");
                exit(1);
        }

        serv_addr.sin_family = AF_INET;
        serv_addr.sin_port = htons(portno);
        serv_addr.sin_addr.s_addr = inet_addr(abcd);

        /* Now connect to the server */
        if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
                perror("ERROR connecting");
                exit(1);
        }

        /* Now ask for a message from the user, this message
                * will be read by server
        */

        printf("Please enter the message: ");
        bzero(buffer,256);
        if (scanf("%255s", buffer) != 1) return 1;

        /* Send message to the server */
        n = write(sockfd, buffer, strlen(buffer));

        if (n < 0) {
                perror("ERROR writing to socket");
                exit(1);
        }

        /* Now read server response */
        bzero(buffer,256);
        n = read(sockfd, buffer, 255);

        if (n < 0) {
                perror("ERROR reading from socket");
                exit(1);
        }

        printf("%s\n",buffer);
        close(sockfd);
        return 0;
}
