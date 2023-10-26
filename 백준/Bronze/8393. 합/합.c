#include <stdio.h>
int main() {
    int n = 0;
    int a = 0;
    scanf("%d", &n);
    for(int i=1; i<n+1; i++) {
        a += i;
    }
    printf("%d", a);
    return 0;
}