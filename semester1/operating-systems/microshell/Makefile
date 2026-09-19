CC = cc
CFLAGS = -std=c11 -Wall -Wextra -Wpedantic

microshell: microshell.c
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f microshell *.o
