#include <stdio.h>

int get_line(char s[],int lim);
// Exercise 2-2. Write a loop equivalent to the for loop below without using &&
// or || .

// for (i=0; i < lim-1 && (c=getchar()) != '\n' && c != EOF; ++i)
// s[i] = c;
//
#define LIMIT 1000

int main() {
   char s[LIMIT];
   while(get_line(s,LIMIT)>0) {
       printf("%s", s);
   }
   return 0;
}

int get_line(char s[],int lim)
{
    int c, i=0;
    // for (i=0; i < lim-1 && (c=getchar()) != '\n' && c != EOF; ++i)
    //   s[i] = c;

    while(i<lim-1) {
       c=getchar();
       if(c==EOF) break;
       if(c=='\n') break;
       s[i++]=c;
    }

    /* end of solution */
    while (c != '\n' && c!=EOF) {
      c=getchar();
      ++i;
    }
    if(c=='\n'&& i<LIMIT-1) 
      s[i++]='\n';
    if(i<LIMIT) s[i] = '\0';
    else s[LIMIT-1] = '\0';
    return i;
}
