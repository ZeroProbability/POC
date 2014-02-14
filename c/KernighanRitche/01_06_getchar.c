#include <stdio.h>

// Exercsise 1-6. Verify that the expression getchar() != EOF is 0 or 1.

int main() {
	int c=0;
	while((c=getchar())!=EOF) {
          printf("%d",c);
          //putchar(c);
        }
        printf("%d",c);
	return 0;
}
