#include <stdio.h>

// Exercise 2-5. Write the function any(s1,s2) , which returns the first 
// location in a string s1 where any character from the string s2 occurs, 
// or -1 if s1 contains no characters from s2 . (The standard library 
// function strpbrk does the same job but returns a pointer to the location.)

int strbrk(char s[], char s1[]);

int main() {
  char instring[]="long string";
  char searchstr[]="tg";
  printf("earliest position of '%s' was %d in '%s' \n", searchstr, 
      strbrk(instring,searchstr), instring);
  return 0;
}

int strbrk(char s[], char s1[])
 {
  int i, j;
  int i1,j1;
  int pos=-1;
  for (i1 = j1 = 0; s1[i1] != '\0'; i1++) {
    for (i = j = 0; s[i] != '\0' && (pos>-1?i<pos:1); i++)
    {
      char c=s1[i1];
      if (s[i] == c) {
        pos=i;
        break;
      }
    }
  }
  return pos;
}
