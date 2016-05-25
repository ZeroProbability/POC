#include <stdio.h>
#include <ctype.h>

#define MAXLENGTH 300

// Exercise 6-1. Our version of getword does not properly handle underscores, 
// string constants, comments, or preprocessor control lines. Write a better 
// version.
//
         
int getword(char *word, int lim); 
int isvalidalnum(char c);
char first_non_space(void);
int getch(void);
void ungetch(int);
void skip_to_newline(void);
void skip_to_endquote(void);
void skip_to_endofcomment(void);

int main() {
  char output[MAXLENGTH];
  getword(output, MAXLENGTH);
  /* TODO: Implement full solution */
  printf("%s\n",output);
  return 0;
}

int getword(char *word, int lim) {
  char *w = word,c;
  c=first_non_space();
  do {
      while(c=='#') {
        skip_to_newline();
        c=first_non_space();
      }
      while(c=='"') {
        skip_to_endquote();
        c=first_non_space();
      }
      while(c=='/') {
        char c1=getch();
        if(c1=='/') skip_to_newline();
        else if(c1=='*') skip_to_endofcomment();
        else ungetch(c1);
        c=first_non_space();
      }
  } while(c=='#' || c=='"' || c=='/');
  if (c != EOF)
    *w++ = c;
  if (!isalpha(c)) {
    *w = '\0';
    return c;
  }
  for ( ; --lim > 0; w++)
    if (!isvalidalnum(*w = getch())) {
      ungetch(*w);
      break;
    }
  *w = '\0';
  return word[0];
}

void skip_to_endofcomment() {
  char c;
  do {
    while ((c = getch())!='*');
    c=getch();
  } while(c!='/');
}

void skip_to_endquote() {
  char c;
  while ((c = getch())!='"');
}

void skip_to_newline() {
  char c;
  while ((c = getch())!='\n');
}

char first_non_space() {
  char c;
  while (isspace(c = getch()));
  return c;
}

int isvalidalnum(char c) {
  if(isalnum(c)) return 1;
  if(c=='_') return 1;
  return 0;
}

