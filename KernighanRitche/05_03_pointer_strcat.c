#include <stdio.h>

void mstrcat(char *s, char *t) {
  while(*s++);
  s--;
  while(*s++=*t++);
}

int main()
{
  char s[100]="some thing here";
  char t[100]="something more here";

  mstrcat(s,t);
  printf("%s",s);
  return 0;
}
