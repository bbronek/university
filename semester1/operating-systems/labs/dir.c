#include <stdio.h>

int main(void) {
    char path[4096];
    if (scanf("%4095s", path) != 1)
        return 1;
    FILE *file = fopen(path, "rb");
    if (file == NULL) {
        perror(path);
        return 1;
    }
    int character = 0, ascii = 1;
    while ((character = fgetc(file)) != EOF) {
        if (character > 127) {
            ascii = 0;
            break;
        }
    }
    if (ferror(file)) {
        fclose(file);
        return 1;
    }
    fclose(file);
    printf("%d\n", ascii);
    return 0;
}
