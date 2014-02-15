#include <stdio.h>

//Exercise 2-4. Write an alternative version of squeeze(s1,s2) that deletes 
//each character in s1 that matches any character in the string s2 .
//
//void squeeze(char s[], int c)
// {
//  int i, j;
//  for (i = j = 0; s[i] != '\0'; i++)
//    if (s[i] != c)
//      s[j++] = s[i];
//  s[j] = '\0';
//}
//

void squeeze(char s[], char s1[]);

int main() {
  char instring[]="long string";
  squeeze(instring,"tgon");
  printf("%s\n", instring);
  return 0;
}

void squeeze(char s[], char s1[])
 {
  int i, j;
  int i1,j1;
  for (i1 = j1 = 0; s1[i1] != '\0'; i1++) {
    for (i = j = 0; s[i] != '\0'; i++)
    {
      char c=s1[i1];
      if (s[i] != c) {
        s[j++] = s[i];
      }
    }
    s[j] = '\0';
  }
}
