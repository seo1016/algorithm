#include <stdio.h>
int main() {
    double a = 0;
    double b = 0;
    scanf("%lf %lf", &a, &b);
    printf("%.100lf", a/b);
    return 0;
}
