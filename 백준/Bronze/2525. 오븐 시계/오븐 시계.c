#include <stdio.h>
int main() {
    int a = 0;
    int b = 0;
    int c = 0;
    scanf("%d %d", &a, &b);
    scanf("%d", &c);
    if(b+c<60) {
        b += c;
    } else if(b+c>=60) {
        b += c;
        a += b/60;
        b %= 60;
    } if(a >= 24) {
        a -= 24;
    }
    printf("%d %d", a, b);

    return 0;
}