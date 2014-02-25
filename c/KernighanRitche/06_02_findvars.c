#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAXLENGTH 300
#define WORDLISTSIZE 300

// Exercise 6-2. Write a program that reads a C program and prints in 
// alphabetical order each group of variable names that are identical in the 
// first 6 characters, but different somewhere thereafter. Don't count words 
// within strings and comments. Make 6 a parameter that can be set
// from the command line.
         
int getword(char *word, int lim); 
int isvalidalnum(char c);
char first_non_space(void);
int getch(void);
void ungetch(int);
void skip_to_newline(void);
void skip_to_endquote(char quotechar);
void skip_to_endofcomment(void);
void addword(char wordlist[WORDLISTSIZE][MAXLENGTH], char* word); 
void sort(char wordlist[WORDLISTSIZE][MAXLENGTH]);

int main(int argc, char *argv[])
{
  char output[MAXLENGTH];
  int length=6,i;
  char wordlist[WORDLISTSIZE][MAXLENGTH];
  for(i=0;i<WORDLISTSIZE;i++) wordlist[i][0]='\0';
  if(argc>1) {
    length=atoi(argv[1]);
    if(length < 1) {
      printf("Error processing argument. Length can not be less than 1\n");
      return 1;
    }
  }
  do {
    getword(output, MAXLENGTH);
    if(isalpha(output[0]) && strlen(output)>length) addword(wordlist, output);
  } while(output[0]!='\0'); 
  sort(wordlist);
  i=1;
  while(wordlist[i][0]!='\0') {
    char v1[10], v2[10];
    memcpy(v1,wordlist[i],length);
    memcpy(v2,wordlist[i-1],length);
    v1[length+1]=v2[length+1]='\0';
    if(strcmp(v1,v2)==0) printf("%s %s\n",wordlist[i-1],wordlist[i]);
    i++;
  }
  return 0;
}

void addword(char wordlist[WORDLISTSIZE][MAXLENGTH], char* word) {
   int i=0;
   while(wordlist[i][0]!='\0' && i<WORDLISTSIZE) {
     if(strcmp(word,wordlist[i])==0) return;
     i++;
   }
   strcpy(wordlist[i], word);
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
        skip_to_endquote('"');
        c=first_non_space();
      }
      while(c=='\'') {
        skip_to_endquote('\'');
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

void skip_to_endquote(char quotechar) {
  char c;
  while ((c = getch())!=quotechar);
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

void sort(char wordlist[WORDLISTSIZE][MAXLENGTH]){
  int i=0,j=0;
  for(;wordlist[i][0]!='\0';i++) {
    for(j=i+1;wordlist[j][0]!='\0';j++) {
      if(strcmp(wordlist[i],wordlist[j])<0) {
        char x[MAXLENGTH];
        strcpy(x,wordlist[i]);
        strcpy(wordlist[i],wordlist[j]);
        strcpy(wordlist[j],x);
      }
    }
  }
}
