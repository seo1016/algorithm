#include <stdio.h>
int main() {
    int n = 0;
    scanf("%d", &n);
    for(int i=1; i<n+1; i++) {
        int j=i;
        while(j!=0) {
            printf("*");
            j--;
        }
        printf("\n");
    }
    return 0;
}