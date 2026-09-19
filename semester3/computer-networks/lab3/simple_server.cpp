#include "../socket_io.h"
#include <arpa/inet.h>
#include <climits>
#include <cstdlib>
#include <iostream>
#include <unistd.h>

int main() {
    int listener = socket(AF_INET, SOCK_STREAM, 0);
    if (listener < 0) {
        perror("socket");
        return 1;
    }
    int reuse = 1;
    setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse));
    sockaddr_in address{};
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8888);
    if (bind(listener, reinterpret_cast<sockaddr *>(&address), sizeof(address)) < 0 ||
        listen(listener, 3) < 0) {
        perror("listen");
        close(listener);
        return 1;
    }
    std::cout << "Waiting for a connection on port 8888..." << std::endl;
    int connection = accept(listener, nullptr, nullptr);
    close(listener);
    if (connection < 0) {
        perror("accept");
        return 1;
    }
    std::string message;
    while (read_line(connection, message)) {
        char *end;
        errno = 0;
        long value = std::strtol(message.c_str(), &end, 10);
        bool valid = errno == 0 && end != message.c_str() && *end == '\0' && value >= INT_MIN &&
                     value < INT_MAX;
        std::string response =
            valid ? std::to_string(value + 1) : "ERROR: expected an integer smaller than INT_MAX";
        if (!send_all(connection, response + "\n"))
            break;
    }
    close(connection);
}
