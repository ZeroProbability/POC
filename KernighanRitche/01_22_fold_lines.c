#include <stdio.h>
#define MAXLINE 1000                       /* maximum input line length */
#define WRAPLENGTH 10 

int get_line(char s[], int lim);
void fold_line(char s[], char out[], int len);
void put_char_at(char out[],int i, char c); 

// Exercise 1-22. Write a program to ``fold'' long input lines into two or more
// shorter lines after the last non-blank character that occurs before the n-th
// column of input. Make sure your program does something intelligent with very
// long lines, and if there are no blanks or tabs before the specified column.

int main()
{
  int len;                                 // Current line length
  char line[MAXLINE]="test\t";             // current input ine
  char folded_line[MAXLINE]="test\t";      // folded line
  
  while ((len = get_line(line, MAXLINE)) > 0) {
      if(len>0){
         fold_line(line, folded_line, len);
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

void fold_line(char s[], char out[], int len){
    int last_space=-1;
    int current_pos_in_column;
    int po=0,i;
    for(i=0,current_pos_in_column=0;i<len;i++, current_pos_in_column++) {
      if(current_pos_in_column==WRAPLENGTH-1 && i+1<len && s[i+1]!='\n') {
        if(last_space==-1) {  // No tabs or spaces found put an - suffix
           put_char_at(out,po++, '-');
           put_char_at(out,po++, '\n');
           put_char_at(out,po++, s[i]); 
        } else {
           if(s[i]==' ' || s[i]=='\t')  {
             put_char_at(out,po++, '\n');
           } else {
             put_char_at(out,po++, s[i]);
             out[last_space]='\n';
           }
        }
        last_space=-1;
        current_pos_in_column=0;
      } else {
         put_char_at(out,po++, s[i]);
      }
      if(out[po-1]==' '|| out[po-1]=='\t') {
        last_space=po-1;
      }
    }
}
