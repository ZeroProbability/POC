#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define MAXLIMIT 80

int getlinex(char s[], int lim);

// Exercise 1-18. Write a program to remove trailing blanks and tabs from each 
// line of input, and to delete entirely blank lines.

int main()
{
  int len;                 // Current line length
  char line[MAXLINE];      // current input ine
  
  while ((len = getlinex(line, MAXLINE)) > 0) {
      int i, last_index_of_non_space=0;
      if(i>MAXLIMIT) i=MAXLIMIT;
      for(i=0;i<len;i++){
         if(line[i]==' ' || line[i]=='\t' || line[i]=='\n' || line[i]=='\0'){
           // nothing
         } else {
             last_index_of_non_space=i;
         }
      }
      line[last_index_of_non_space+1]='\0';
      printf("%s|\n", line);
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
