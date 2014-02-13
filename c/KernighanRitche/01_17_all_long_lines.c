#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define MAXLIMIT 80

int getlinex(char s[], int lim);

/* print the longest input line */
int main()
{
  int len;                 // Current line length
  char line[MAXLINE];      // current input ine
  
  while ((len = getlinex(line, MAXLINE)) > 0) {
    if (len > 80) 
        printf("%s", line);
  }
  return 0;
}

/* getline: read a line into s, return length */
int getlinex(char s[],int lim)
{
    int c, i;
    for (i=0; i < lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
      s[i] = c;
    while (c != '\n' && c!=EOF) {
      c=getchar();
      ++i;
    }
    if(c=='\n'&& i<MAXLINE-1) 
      s[i++]='\n';
    if(i<MAXLINE) s[i] = '\0';
    else s[MAXLINE-1] = '\0';
    return i;
}
