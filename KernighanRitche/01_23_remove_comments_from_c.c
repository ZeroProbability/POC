#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define WRAPLENGTH 10 

int get_line(char s[], int lim);
void process_line(char s[], char out[], int len);
void put_char_at(char out[],int i, char c); 

int inside_comment=0;
int inside_string=0;

// Exercise 1-23. Write a program to remove all comments from a C program. 
// Don't forget to handle quoted strings and character constants properly. 
// C comments don't nest.

int main()
{
  int len;                                 // Current line length
  char line[MAXLINE]="";             // current input ine
  char folded_line[MAXLINE]="";      // folded line
  
  while ((len = get_line(line, MAXLINE)) > 0) {
      if(len>0){
         process_line(line, folded_line, len);
      }
      printf("%s",folded_line);
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

void process_line(char s[], char out[], int len){
    int po=0,i;
    for(i=0;i<len;i++) {
          if(inside_comment) {
             if(s[i]=='*' && s[i+1]=='/') {
                 i++;
                 inside_comment=0;
             }
          } else if(inside_string) {
                if(s[i]=='"') {
                  inside_string=0;
                }
                put_char_at(out,po++, s[i]);
          } else {
                if(s[i]=='/' && s[i+1]=='/')  {
                  put_char_at(out, po++, '\n');
                  return;
                }
                if(s[i]=='"') {
                  inside_string=1;
                  put_char_at(out, po++, s[i]);
                } else if(s[i]=='/' && s[i+1]=='*')  {
                  inside_comment=1;
                } else {
                  put_char_at(out, po++, s[i]);
                }
           }
     } 
}
