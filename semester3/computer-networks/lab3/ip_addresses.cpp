#include <arpa/inet.h>
#include <cstdint>
#include <cstdio>

int main() {
    char input[INET_ADDRSTRLEN];
    in_addr address{};
    std::printf("Enter an IPv4 address (a.b.c.d): ");
    if (std::scanf("%15s", input) != 1 || inet_pton(AF_INET, input, &address) != 1) {
        std::fputs("Invalid IPv4 address\n", stderr);
        return 1;
    }
    uint32_t value = ntohl(address.s_addr);
    std::printf("Host-order value: %u, hex=%08X\n", value, value);
    std::printf("Bytes: %u %u %u %u\n", value >> 24, (value >> 16) & 255,
                (value >> 8) & 255, value & 255);
}
