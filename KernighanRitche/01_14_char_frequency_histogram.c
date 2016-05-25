#include <stdio.h> 
#include <unistd.h>

#define CHAR_SIZE 256

// Exercise 1-14. Write a program to print a histogram of the frequencies of
// different characters in its input.

int main() {
  int c=0;
  int count_lookup[CHAR_SIZE];   // we are assuming that the word size will never exceed CHAR_SIZE
  int max_count=0;

  int i;

  for(i=0;i<CHAR_SIZE;i++) count_lookup[i]=0; // init the array
  
  while((c=getchar())!=EOF) {
     count_lookup[c]++;
     if(max_count<count_lookup[c]) max_count=count_lookup[c];
  }
  for(i=0;i<CHAR_SIZE;i++) {
     if(count_lookup[i]>0) {
          printf("ascii:%3d(%c)  |",i,i);
          int j;
          for(j=0;j<(count_lookup[i]*50)/max_count;j++) {
              putchar('*');
          }
          printf("%d\n",count_lookup[i]);
     }
  }

  return 0;
}
