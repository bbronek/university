#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <sys/socket.h>
#include <arpa/inet.h> 
#include <unistd.h>    

int main(int argc, char *argv[])
{
       int socket_desc, client_sock, c, read_size;
       struct sockaddr_in server, client;
       char client_message[2000];
       int out;

       //Create socket
       socket_desc = socket(AF_INET, SOCK_STREAM, 0);
       if (socket_desc == -1)
       {
              printf("Could not create socket");
       }
       puts("Socket created");

       //Prepare the sockaddr_in structure
       server.sin_family = AF_INET;
       server.sin_addr.s_addr = INADDR_ANY;
       server.sin_port = htons(8888);

       //Bind
       if (bind(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
       {
              //print the error message
              perror("bind failed. Error");
              return 1;
       }
       puts("bind done");

       //Listen
       listen(socket_desc, 3);

       //Accept and incoming connection
       puts("Waiting for incoming connections...");
       c = sizeof(struct sockaddr_in);

       //accept connection from an incoming client
       client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t *)&c);
       if (client_sock < 0)
       {
              perror("accept failed");
              return 1;
       }
       puts("Connection accepted");

       //Receive a message from client
       int length;
       while ((read_size = recv(client_sock, client_message, 2000, 0)) > 0)
       {
              //Send client number + 1
              out = atoi(client_message) + 1;
              sprintf(client_message, "%d", out);
              write(client_sock, client_message, strlen(client_message));
       }

       if (read_size == 0)
       {
              puts("Client disconnected");
              fflush(stdout);
       }
       else if (read_size == -1)
       {
              perror("recv failed");
       }

       return 0;
}
