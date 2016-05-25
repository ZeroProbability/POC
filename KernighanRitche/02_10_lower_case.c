#include <stdio.h>

// Exercise 2-10. Rewrite the function lower , which converts upper case 
// letters to lower case, with a conditional expression instead of if-else .

char lower(char x);

int main() {
   printf("%c\n",lower('x'));
   printf("%c\n",lower('X'));

  return 0;
}

char lower(char x){
    return (x>='A'&&x<='Z')?x+('a'-'A'):x;
}
