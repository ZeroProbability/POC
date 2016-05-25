#include <ctype.h>
#include <stdio.h>

#define BUFSIZE 100
char buf[BUFSIZE];
int bufp = 0;
/* buffer for ungetch */
/* next free position in buf */
int getch(void) /* get a (possibly pushed-back) character */
{
  return (bufp > 0) ? buf[--bufp] : getchar();
}
void ungetch(int c)
  /* push character back on input */
{
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else {
    if(c==EOF && bufp>0) {
                 // there are characters already in buffer. 
                 // they wont be processed if EOF is pushed in. 
        if(buf[0]==EOF) {
          printf("warning: EOF already in buffer, ignored. ");
          return ;
        }
        int i=bufp;
        while(i>0) {
          buf[i]=buf[i-1];
          i--;
          buf[0]=EOF;
        } 
        bufp++;
    } else {
      buf[bufp++] = c;
    }
  }
}
