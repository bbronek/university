#ifndef UNIVERSITY_SOCKET_IO_H
#define UNIVERSITY_SOCKET_IO_H

#include <cerrno>
#include <string>
#include <sys/socket.h>

inline bool send_all(int socket, const std::string &message) {
    size_t sent = 0;
    while (sent < message.size()) {
        ssize_t count = send(socket, message.data() + sent, message.size() - sent, MSG_NOSIGNAL);
        if (count < 0 && errno == EINTR)
            continue;
        if (count <= 0)
            return false;
        sent += static_cast<size_t>(count);
    }
    return true;
}

inline bool read_line(int socket, std::string &line) {
    line.clear();
    while (line.size() <= 1024) {
        char character;
        ssize_t count = recv(socket, &character, 1, 0);
        if (count < 0 && errno == EINTR)
            continue;
        if (count <= 0)
            return false;
        if (character == '\n')
            return true;
        line += character;
    }
    errno = EMSGSIZE;
    return false;
}

#endif
