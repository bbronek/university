#include <netinet/in.h>
#include <sys/socket.h>
#include <stdio.h>
#include <arpa/inet.h>

int main(void) {
        char abcd[512];
        unsigned long adress;
        unsigned char *bytes =
        (unsigned char*) &adress;

        printf("Write IP adress in format a.b.c.d: ");

        scanf("%s",abcd);
        adress = inet_addr(abcd);

        if (adress == 0xffffffff) {
                printf("Invalid IP!\n");
                return 1;
        }
        printf("Network format to %lu, hex=%lX\n",adress, adress);

        printf("bytes (hex): %X %X %X %X\n",
                bytes[3], bytes[2], bytes[1], bytes[0]);

        printf("bytes (dec): %u %u %u %u\n",
                bytes[3], bytes[2], bytes[1], bytes[0]);
        return 0;
}
