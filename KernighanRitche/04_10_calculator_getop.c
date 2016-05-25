#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define NUMBER  0 /* signal that a number was found */
#define MAXLENGTH 1000

/* getop: get next character or numeric operand */
char getch(); 

char inputline[MAXLENGTH];
int inputline_position=0;
size_t inputline_length=0;

int getop(char s[])
{
  int i, c, isnumber=0;
  while ((s[0] = c = getch()) == ' ' || c == '\t')
    ;
  if(c=='-' || c=='+') {
    char cn=getch();
    if(isdigit(cn)) isnumber=1;
    inputline_position--;
  }
  if (isnumber || isdigit(c) || c == '.')  {
    // nothing - it is a number
  } else {
    return c; 
  }
  s[1] = '\0';
  i = 0;

  if(c=='-' || c=='+') {
    s[++i]=c=getch();
    s[i+1]='\0';
  }

  if (isdigit(c)) /* collect integer part */
    while (isdigit(s[++i] = c = getch()))
      ;
  if (c == '.') /* collect fraction part */
    while (isdigit(s[++i] = c = getch()))
      ;
  s[i] = '\0';
  if (c != EOF)
    inputline_position--;
  return NUMBER;
}

char getch() {
  char* c;
  if(inputline_position==(int)inputline_length) {
      c=fgets(inputline,MAXLENGTH, stdin);
      if(c==NULL) return EOF;
      inputline_length=strlen(inputline);
      inputline_position=0;
  }
  return inputline[inputline_position++];
}
