#include <stdio.h>

// Exercise 4-2. Extend atof to handle scientific notation of the form
//      123.45e-6
// where a floating-point number may be followed by e or E and an optionally 
// signed exponent.

double atof(char s[]);
int isdigit(int c) ;
int isspace(int c) ;

int main() {

  printf("%e", atof("100.02e-2\n"));

  return 0;
}

double atof(char s[])
{
  double val, power;
  int i, sign,expsign,exp;
  for (i = 0; isspace(s[i]); i++) /* skip white space */
    ;
  sign = (s[i] == '-') ? -1 : 1;
  if (s[i] == '+' || s[i] == '-')
    i++;
  for (val = 0.0; isdigit(s[i]); i++)
    val = 10.0 * val + (s[i] - '0');
  if (s[i] == '.')
    i++;
  for (power = 1.0; isdigit(s[i]); i++) {
    val = 10.0 * val + (s[i] - '0');
    power *= 10;
  }
  if (s[i] == 'e' || s[i]== 'E') {
      i++;
      expsign = (s[i] == '-') ? -1 : 1;
      if (s[i] == '+' || s[i] == '-')
        i++;
      for (exp = 0; isdigit(s[i]); i++) {
        exp=10*exp+(s[i]-'0');
      }
      int j;
      for(j=0;j<exp;j++) {
        if(expsign>0) val*=10;
        else val/=10;
      }
  }
  return sign * val / power;
}
