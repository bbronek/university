#include <stdio.h>

int main(void) {
    float apple_count, apple_price, orange_price, total_price;
    scanf("%f%f%f%f", &apple_count, &apple_price, &orange_price, &total_price);
    printf("%.2f", (total_price - (apple_price * apple_count)) / orange_price);

    return 0;
}
