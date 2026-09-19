#include <stdio.h>
#include <string.h>

int main(void) {
    short case_count = 0, people_count = 0, outgoing_count = -1;

    if (scanf("%hd", &case_count) != 1)
        return 1;
    for (int i = 0; i < case_count; ++i) {
        if (scanf("%hd", &people_count) != 1)
            return 1;
        if (people_count <= 0 || people_count > 1000)
            return 1;
        int connections[people_count + 2][people_count];
        memset(connections, 0, sizeof(connections[0][0]) * (people_count + 2) * people_count);
        for (int d = 0; d < people_count; ++d) {
            outgoing_count = -1;
            for (int j = 0; j < people_count; ++j) {
                if (scanf("%d", &connections[d][j]) != 1)
                    return 1;
                if (connections[d][j]) {
                    outgoing_count += 1;
                    connections[people_count][j]++;
                }
            }
            connections[people_count + 1][d] = outgoing_count;
        }

        for (int x = 0; x < people_count; ++x) {
            if (connections[people_count + 1][x] == 0 &&
                connections[people_count][x] == people_count) {
                printf("%hd", (x + 1));
                break;
            }
        }
    }

    return 0;
}
