#include <stdio.h>
int main() {
    int h = 0;
    int m = 0;
    scanf("%d %d", &h, &m);
    if(m-45>=0 && h>=0) {
        m -= 45;
    } else if(m-45<0){
        h -= 1;
        m += 15;
    } if(h<0) {
        h += 24;
    }
    printf("%d %d", h, m);
}