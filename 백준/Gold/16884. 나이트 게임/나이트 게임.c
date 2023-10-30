#include <stdio.h>
int main() {
    int t = 0;
    int n = 0;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        scanf("%d", &n);
        if(n%2==0) {
            printf("cubelover\n");
        } else {
            printf("koosaga\n");
        }
    }
    return 0;
}