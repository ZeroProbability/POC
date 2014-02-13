#include <stdio.h> 
#include <unistd.h>

#define WORD_MAX_SIZE 100

int main() {
  int c=0;
  int current_word_size=0;
  int size_lookup[WORD_MAX_SIZE];   // we are assuming that the word size will never exceed WORD_MAX_SIZE
  int max_count=0;

  int i;

  for(i=0;i<WORD_MAX_SIZE;i++) size_lookup[i]=0; // init the array
  
  while(c!=EOF) {
     c=getchar();

     if((c>='a' && c<='z') || (c>='A' && c<='Z') || (c>='0' && c<='9')) {
       current_word_size++;
     } else {
       if(current_word_size>0) {
           if(current_word_size < WORD_MAX_SIZE){ // ignore any word size > 100
               size_lookup[current_word_size]++; 
               if(size_lookup[current_word_size]>max_count) max_count=size_lookup[current_word_size];
           } else  {
               printf("Warning: word size %d ignored because the program can only handle %d word size.\n", current_word_size, WORD_MAX_SIZE); 
           }
           current_word_size=0;
       } 
    }
  }
  for(i=0;i<WORD_MAX_SIZE;i++) {
     if(size_lookup[i]>0) {
          printf("%5d  |",i);
          int j;
          for(j=0;j<(size_lookup[i]*50)/max_count;j++) {
              putchar('*');
          }
          printf("%d\n",size_lookup[i]);
     }
  }

  return 0;
}
