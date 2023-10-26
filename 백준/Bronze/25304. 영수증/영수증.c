#include <stdio.h>
int main() {
    int x = 0;
    int n = 0;
    int a = 0;
    int b = 0;
    int sum = 0;
    scanf("%d", &x);
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d %d", &a, &b);
        sum += a*b;
    }

    if(x==sum) {
        printf("Yes");
    } else {
        printf("No");
    }
    return 0;
}