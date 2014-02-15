#include <stdio.h>

#define MAXLENGTH 1000
//Exercise 3-2. Write a function escape(s,t) that converts characters like 
//newline and tab into visible escape sequences like \n and \t as it copies 
//the string t to s . Use a switch . Write a function for the other direction 
//as well, converting escape sequences into the real characters.
//
void escape(char s[], char t[]) ;
void deescape(char s[], char t[]) ;

int main() {
  char s[MAXLENGTH]="some \t  \t \ttext goes \nhere";
  char t[MAXLENGTH];
  char t1[MAXLENGTH];

  escape(s,t);
  printf("%s\n",s);
  printf("%s\n",t);
  deescape(t, t1);
  printf("%s\n",t1);
  return 0;
}

void escape(char s[], char t[]) {
  int i=0,j=0;
  while(s[i]!=0) {
    switch(s[i]) {
      case '\t': t[j++]='\\';t[j++]='t';break;
      case '\n': t[j++]='\\';t[j++]='n';break;
      default: t[j++]=s[i];
    }
    i++;
  }
  t[j]=0;
}

void deescape(char s[], char t[]) {
  int i=0,j=0;
  while(s[i]!=0) {
    if(s[i]=='\\') {
      switch(s[i+1]) {
        case 't': t[j++]='\t';i++;break;
        case 'n': t[j++]='\n';i++;break;
        default: t[j++]='\\';
      }
    } else {
        t[j++]=s[i];
    }
    i++;
  }
  t[j]=0;
}
