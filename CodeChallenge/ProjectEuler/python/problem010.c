#include <stdio.h>
#include <malloc.h>

int* prime_sieve(int n, int *a) {

    int c;
    for(c=0; c< n; c++) {
        a[c] = 1;
    }
    a[0] = a[1] = 0;

    for(c=2; c<n; c++) {
        if(a[c]) {
            int c1;
            for(c1=c*c; c1 <n ; c1+=c) {
                a[c1] = 0;
            }
        }
    }
    return a;
}

void compute_sum(int n)
{
    n++;
    int *a;
    a=(int *)malloc(n * sizeof(int));
    int *ps = prime_sieve(n, a);
    free(a);
    int i;
    long sum=0;
    for (i=0; i < n; i++) {
        if(ps[i]) {
            sum+=i;
        }
    }
    printf("%ld\n", sum);
    
}

void read_tests() {
    int number_of_tests;
    scanf("%d", &number_of_tests);

    int i;
    int n;
    for(i=0; i<number_of_tests; i++) {
        scanf("%d", &n);
        compute_sum(n);
    }
}


int main(void)
{
    read_tests();
    return 0;
}
