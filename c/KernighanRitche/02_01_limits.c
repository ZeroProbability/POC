#include <stdio.h>
#include <limits.h>
#include <float.h>

// Exercise 2-1. Write a program to determine the ranges of char , short , int,
// and long variables, both signed and unsigned , by printing appropriate 
// values from standard headers and by direct computation. Harder if you 
// compute them: determine the ranges of the various floating-point types.

int main() {
  printf("signed char: %d %d\n",CHAR_MIN, CHAR_MAX);
  printf("unsigned char: %d %d\n\n",0, UCHAR_MAX);

  printf("signed int: %d %d\n",INT_MIN, INT_MAX);
  printf("unsigned int: %u %u\n\n",0, UINT_MAX);

  printf("signed long: %ld %ld\n",LONG_MIN, LONG_MAX);
  printf("unsigned long: %lu %lu\n\n",0L, ULONG_MAX);

  printf("signed short: %hd %hd\n",SHRT_MIN, SHRT_MAX);
  printf("unsigned short: %hu %hu\n\n",0, USHRT_MAX);
 
  printf("float: %f %f\n",FLT_MIN, FLT_MAX);
  printf("double: %lf %lf\n",DBL_MIN, DBL_MAX);
  printf("longdouble: %Lf %Lf\n",LDBL_MIN, LDBL_MAX);

  printf("TODO - find out computationally ... ");

  return 0;
}
