#include <stdio.h>
int main() {
    long double a = 0;
    long double b = 0;
    scanf("%LG %LG", &a, &b);
    printf("%.100LG", a/b);
    return 0;
}
