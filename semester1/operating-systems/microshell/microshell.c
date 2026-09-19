#define _POSIX_C_SOURCE 200809L
#include <ctype.h>
#include <errno.h>
#include <fcntl.h>
#include <limits.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

static int parse_arguments(char *line, char **arguments, size_t capacity) {
  char *read = line, *write = line;
  size_t count = 0;
  while (*read != '\0') {
    while (isspace((unsigned char)*read))
      ++read;
    if (*read == '\0')
      break;
    if (count + 1 >= capacity)
      return -1;
    arguments[count++] = write;
    char quote = '\0';
    while (*read != '\0') {
      char character = *read++;
      if (quote != '\0') {
        if (character == quote)
          quote = '\0';
        else
          *write++ = character;
      } else if (character == '\'' || character == '"') {
        quote = character;
      } else if (isspace((unsigned char)character)) {
        break;
      } else if (character == '\\' && *read != '\0') {
        *write++ = *read++;
      } else {
        *write++ = character;
      }
    }
    if (quote != '\0')
      return -1;
    *write++ = '\0';
  }
  arguments[count] = NULL;
  return (int)count;
}

static void change_directory(int count, char **arguments) {
  static char previous[PATH_MAX] = "";
  char current[PATH_MAX];
  if (count > 2) {
    fputs("Usage: cd [directory | ~ | -]\n", stderr);
    return;
  }
  const char *destination = count == 1 || strcmp(arguments[1], "~") == 0
                                ? getenv("HOME")
                            : strcmp(arguments[1], "-") == 0 ? previous
                                                             : arguments[1];
  if (destination == NULL || *destination == '\0') {
    fputs("No destination directory is available\n", stderr);
    return;
  }
  if (getcwd(current, sizeof current) == NULL || chdir(destination) != 0) {
    perror("cd");
    return;
  }
  strcpy(previous, current);
}

static void execute(int count, char **arguments) {
  char *destination = NULL;
  for (int index = 0; index < count; ++index) {
    if (strcmp(arguments[index], ">") == 0) {
      if (index == 0 || index != count - 2) {
        fputs("Usage: command [arguments] > file\n", stderr);
        return;
      }
      destination = arguments[index + 1];
      arguments[index] = NULL;
      break;
    }
  }
  pid_t child = fork();
  if (child == -1) {
    perror("fork");
    return;
  }
  if (child == 0) {
    signal(SIGINT, SIG_DFL);
    if (destination != NULL) {
      int file = open(destination, O_WRONLY | O_CREAT | O_TRUNC, 0666);
      if (file == -1 || dup2(file, STDOUT_FILENO) == -1) {
        perror(destination);
        _exit(1);
      }
      close(file);
    }
    execvp(arguments[0], arguments);
    perror(arguments[0]);
    _exit(127);
  }
  while (waitpid(child, NULL, 0) == -1) {
    if (errno != EINTR) {
      perror("waitpid");
      break;
    }
  }
}

int main(void) {
  char *line = NULL;
  size_t capacity = 0;
  char *arguments[128];
  bool interactive = isatty(STDIN_FILENO);
  signal(SIGINT, SIG_IGN);
  for (;;) {
    if (interactive) {
      char directory[PATH_MAX];
      printf("%s $ ",
             getcwd(directory, sizeof directory) == NULL ? "?" : directory);
      fflush(stdout);
    }
    if (getline(&line, &capacity, stdin) == -1)
      break;
    int count = parse_arguments(line, arguments,
                                sizeof arguments / sizeof arguments[0]);
    if (count < 0) {
      fputs("Unclosed quote or too many arguments\n", stderr);
    } else if (count == 0) {
      continue;
    } else if (strcmp(arguments[0], "exit") == 0) {
      break;
    } else if (strcmp(arguments[0], "cd") == 0) {
      change_directory(count, arguments);
    } else if (strcmp(arguments[0], "help") == 0) {
      puts("Microshell by Bartosz Bronikowski\n"
           "Built-ins: cd [directory | ~ | -], help, exit\n"
           "Other commands, including grep and sort, run through PATH.\n"
           "Single and double quotes group arguments. Use > file to redirect "
           "output.\n"
           "Pipelines, variable expansion, and job control are not supported.");
    } else {
      execute(count, arguments);
    }
  }
  free(line);
  return 0;
}
