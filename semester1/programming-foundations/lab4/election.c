#include <stdio.h>

int max(int votes[], int candidate_count) {
    int vote_count = 1, winner = 1;
    for (int i = 1; i <= candidate_count; ++i) {
        if (votes[i] > vote_count) {
            vote_count = votes[i];
            winner = i;
        }
    }
    return winner;
}

int main(void) {
    int candidate_count = 0, vote_count = 0, candidate = 0;
    if (scanf("%d%d", &candidate_count, &vote_count) != 2)
        return 1;
    int votes[candidate_count + 1];
    for (int i = 1; i <= candidate_count; ++i) {
        votes[i] = 0;
    }
    for (int i = 0; i < vote_count; ++i) {
        if (scanf("%d", &candidate) != 1)
            return 1;
        votes[candidate]++;
    }
    for (int j = 1; j <= candidate_count; ++j) {
        printf("%d:%d ", j, votes[j]);
    }
    printf("%d", max(votes, candidate_count));

    return 0;
}
