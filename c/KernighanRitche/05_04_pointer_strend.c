#include <stdio.h>

int mstrend(char *s, char *t) {
  char *t1=t;
  while(*t1++); // go to end of the string
  while(*s++);

  while(t<t1) 
    if(*--t1!=*--s) return 0;
  return 1;
}

int main()
{
  char s[100]="some thing here";
  char t[100]="thing here";

  if(mstrend(s,t)) 
    printf("is at the end\n");
  else 
    printf("is not at the end\n");
  return 0;
}
