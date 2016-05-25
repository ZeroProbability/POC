#include <stdio.h>
#include <limits.h>

// Exercise 2-9. In a two's complement number system, x &= (x-1) deletes the 
// rightmost 1-bit in x . Explain why. Use this observation to write a faster 
// version of bitcount .
// int bitcount(unsigned x)
// {
//   int b;
//   for (b = 0; x != 0; x >>= 1)
//      if (x & 01)
//         b++;
//   return b;
// }
//
// Ans: 1 & (1-1) = 0
//      2 & (2-1) = 0
//      4 & (4-1) = 0
//      8 & (8-1) = 0
//
//      So, successive x & (x-1) operation will keep removing the rightmost 
//      non-zeo bit from the integer. 

int bitcount(unsigned x);

int main() {
  printf("%d\n", bitcount(6));
  printf("%d\n", bitcount(UINT_MAX));

  return 0;
}

int bitcount(unsigned x){
   int b;
   for(b=0; x!=0; x&=(x-1)) b++;
   return b;
}
