#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define TABLENGTH 8

int get_line(char s[], int lim);
void detab_line(char s[], char out[], int len);
void put_char_at(char out[], int i, char c);

// Exercise 1-20. Write a program detab that replaces tabs in the input with 
// the proper number of blanks to space to the next tab stop. Assume a fixed 
// set of tab stops, say every n columns. Should n be a variable or a symbolic 
// parameter?

/* print the longest input line */
int main()
{
  int len;                 // Current line length
  char line[MAXLINE]="test\t";      // current input ine
  char detabed_line[MAXLINE];      // detabbed line
  
  detab_line(line,detabed_line, 5);
  while ((len = get_line(line, MAXLINE)) > 0) {
      if(len>0){
         detab_line(line, detabed_line, len);
      }
      printf("%s",detabed_line);
  }
  return 0;
}

/* getline: read a line into s, return length */
int get_line(char s[],int lim)
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

void put_char_at(char out[],int i, char c) {
   if(i<MAXLINE-1) {
       out[i]=c;
       out[i+1]=0;
   }
}

void detab_line(char s[], char out[], int len) {
    int po=0,i=0;
    for(i=0;i<len;i++) {
       if(s[i]=='\t') {
          int space_count=TABLENGTH-po%TABLENGTH;
          int j=0;
          for(j=0;j<space_count;j++) {
             put_char_at(out, po++, ' ');
          }
       } else {
           put_char_at(out, po++, s[i]);
       }
    }
}
