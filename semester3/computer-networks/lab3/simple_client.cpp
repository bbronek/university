#include "../socket_io.h"
#include <arpa/inet.h>
#include <iostream>
#include <unistd.h>

int main() {
    std::string host, message;
    int port;
    std::cout << "Server IPv4 address: ";
    if (!(std::cin >> host))
        return 1;
    std::cout << "Server port: ";
    if (!(std::cin >> port) || port < 1 || port > 65535)
        return 1;
    sockaddr_in address{};
    address.sin_family = AF_INET;
    address.sin_port = htons(port);
    if (inet_pton(AF_INET, host.c_str(), &address.sin_addr) != 1) {
        std::cerr << "Invalid IPv4 address\n";
        return 1;
    }
    int connection = socket(AF_INET, SOCK_STREAM, 0);
    if (connection < 0) {
        perror("socket");
        return 1;
    }
    if (connect(connection, reinterpret_cast<sockaddr *>(&address), sizeof(address)) < 0) {
        perror("connect");
        close(connection);
        return 1;
    }
    std::cout << "Enter an integer: ";
    if (!(std::cin >> message) || !send_all(connection, message + "\n") ||
        !read_line(connection, message)) {
        std::cerr << "Message exchange failed\n";
        close(connection);
        return 1;
    }
    std::cout << message << '\n';
    close(connection);
}
