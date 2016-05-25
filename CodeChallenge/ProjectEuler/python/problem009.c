#include <stdio.h>

void find_max(long n) {
    long a, b, c;
    long max=-1;
    for(a=3; a < n /3 ; a++) {
        for (b = a + 1; b < n * 2 / 3; b++) {
            c = n - a - b;
            if((a  + b) > c && (a + c) > b && (b + c) > a) {
                // nop
            } else {
                break;
            }
             if(c < b) break;
             if (a * a + b * b == c * c) {
                 if (a * b * c > max) 
                     max = a * b * c;
             }
        }
    }
    printf("%ld\n", max);
}

void read_tests() {
    int number_of_tests;
    scanf("%d", &number_of_tests);

    int i;
    int n;
    for(i=0; i<number_of_tests; i++) {
        scanf("%d", &n);
        find_max(n);
    }
}


int main(void)
{
    read_tests();
    return 0;
}
