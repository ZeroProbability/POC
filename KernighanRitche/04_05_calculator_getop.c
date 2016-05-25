#include <ctype.h>
#include <stdio.h>

#define NUMBER  0 /* signal that a number was found */

int getch(void);
void ungetch(int);
/* getop: get next character or numeric operand */

int getop(char s[])
{
  int i, c, isnumber=0;
  while ((s[0] = c = getch()) == ' ' || c == '\t')
    ;
  if(c=='-' || c=='+') {
    char cn=getch();
    if(isdigit(cn)) isnumber=1;
    ungetch(cn);
  }
  if (isnumber || isdigit(c) || c == '.')  {
    // nothing - it is a number
  } else {
    return c; 
  }
  s[1] = '\0';
  i = 0;

  if(c=='-' || c=='+') {
    s[++i]=c=getch();
    s[i+1]='\0';
  }

  if (isdigit(c)) /* collect integer part */
    while (isdigit(s[++i] = c = getch()))
      ;
  if (c == '.') /* collect fraction part */
    while (isdigit(s[++i] = c = getch()))
      ;
  s[i] = '\0';
  if (c != EOF)
    ungetch(c);
  return NUMBER;
}

