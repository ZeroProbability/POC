#include <stdio.h>

int main() {
	int c=0;
	while((c=getchar())!=EOF) {
          printf("%d",c);
          //putchar(c);
        }
        printf("%d",c);
	return 0;
}
