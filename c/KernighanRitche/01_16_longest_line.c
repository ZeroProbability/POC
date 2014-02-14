#include <stdio.h>
#define MAXLINE 10                       /* maximum input line length */

int getlinex(char s[], int lim);
void copy(char to[], char from[]);

// Exercise 1-16. Revise the main routine of the longest-line program so it 
// will correctly print the length of arbitrary long input lines, and  as 
// much as possible of the text.
int main()
{
  int len;                 // Current line length
  int max;                 // Maximum length so far
  char line[MAXLINE];      // current input ine
  char longest[MAXLINE];   /* longest line saved here */
  
  max = 0;
  while ((len = getlinex(line, MAXLINE)) > 0)
    if (len > max) {
      max = len;
      copy(longest, line);
    }
  if (max > 0) /* there was a line */
      printf("lenth %d for line :%s", max, longest);
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

/* copy: copy 'from' into 'to'; assume to is big enough */
void copy(char to[], char from[])
{
  int i;
  i = 0;
  while ((to[i] = from[i]) != '\0')
    ++i;
}
