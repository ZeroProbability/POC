#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define TABLENGTH 8

int get_line(char s[], int lim);
void entab_line(char s[], char out[], int len);
void put_char_at(char out[], int i, char c);

// Exercise 1-21. Write a program entab that replaces strings of blanks by the 
// minimum number of tabs and blanks to achieve the same spacing. Use the same 
// tab stops as for detab . When either a tab or a single blank would suffice 
// to reach a tab stop, which should be given preference?

int main()
{
  int len;                 // Current line length
  char line[MAXLINE]="test\t";      // current input ine
  char entabed_line[MAXLINE];      // entabed line
  
  while ((len = get_line(line, MAXLINE)) > 0) {
      if(len>0){
         entab_line(line, entabed_line, len);
      }
      printf("%s",entabed_line);
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

void entab_line(char s[], char out[], int len) {
    int po=0,i=0;
    for(i=0;i<len;i++) {
       if(s[i]==' ') {
          int k=i+1;
          for(;k<len && s[k]==' ';k++){
            if(k%TABLENGTH==0) {
                put_char_at(out, po++, '\t');
                i=k;
            }
          }
          int k1;
          for(k1=i; k1<k; k1++) {  // there are spaces but not enough to replace with tabs
            put_char_at(out, po++, ' '); i++;
          }
          i--; // value of i is one more than what it should be
       } else {
           put_char_at(out, po++, s[i]);
       }
    }
}
