#include <ctype.h>
#include <stdio.h>

int getch(void);
void ungetch(int);

/* getfloat: get next float from input into *pn */
int getfloat(float *pn)
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
    if(c=='.') {
      float exp=10;
      for (c=getch(); isdigit(c); c = getch(),exp*=10)
        *pn = *pn + ((float)(c - '0'))/exp;
    }
    *pn *= sign;
    if (c != EOF)
      ungetch(c);
    return c;
}

int main()
{
  float x=0;
  getfloat(&x);
  printf("got float:%f\n",x);
  return 0;
}
