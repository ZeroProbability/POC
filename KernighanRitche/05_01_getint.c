#include <ctype.h>
#include <stdio.h>

int getch(void);
void ungetch(int);

/* getint: get next integer from input into *pn */
int getint(int *pn)
{
    int c, sign;
    while (isspace(c = getch())) /* skip white space */
      ;
    if (!isdigit(c) && c != EOF && c != '+' && c != '-') {
      ungetch(c); /* it is not a number */
      return 0;
    }
    sign = (c == '-') ? -1 : 1;

    if (c == '+' || c == '-'){
      int c1 = getch();
      if(!isdigit(c1)) { /* again - not a number */
        ungetch(c1);
        ungetch(c);
        return 0;
      } else {
        c=c1;
      }
    }

    for (*pn = 0; isdigit(c); c = getch())
      *pn = 10 * *pn + (c - '0');
    *pn *= sign;
    if (c != EOF)
      ungetch(c);
    return c;
}

int main()
{
  int x=0;
  getint(&x);
  printf("got integer:%d\n",x);
  return 0;
}
