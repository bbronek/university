#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
#define BUFFER_SIZE 4028

int main(void) {
  const char s[2] = " ";
  char *token;
  char line[512];
  int size = 0;
  while (fgets(line, sizeof(line), stdin) != NULL) {
    size++;
    if (size > 1) {
      int c = 0;
      token = strtok(line, s);
      while (token != NULL) {
        c++;
        if (c == 3) {
          printf("%s\n", token);
        } else if (c > 3)
          break;
        token = strtok(NULL, s);
      }
    }
  }

  return 0;
}
