#include <stdio.h>

void mstrncpy(char* c, char* t, int n) {
  int i=0;
  while(i++<n && (*t++=*c++) !=0);
}

void mstrncat(char* c, char* t, int n) {
  int i=0;
  while(*t++);
  t--;
  while(i++<n && (*t++=*c++) !=0);
}

int mstrncmp(char* c, char* t, int n) {
  int i=0;
  while(i++<n) 
    if(*t++!=*c++) return 0;
  return 1;
}

int main()
{
  char s[100]="<namex string";
  char t[100]="<anbu7 string";

  mstrncpy(s,t,5);
  printf("changed string: %s\n", t);

  mstrncat(s,t,5);
  printf("changed string: %s\n", t);

  printf("return value of compare %d\n",mstrncmp(s,t,5));
  printf("return value of compare %d\n",mstrncmp(s,t,6));
  return 0;
}
