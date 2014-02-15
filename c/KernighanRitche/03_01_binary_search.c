#include <stdio.h>

// Exercise 3-1. Our binary search makes two tests inside the loop, when one 
// would suffice (at the price of more tests outside.) Write a version with 
// only one test inside the loop and measure the difference in run-time.
//
/* binsearch: find x in v[0] <= v[1] <= ... <= v[n-1] */
//
//      int binsearch(int x, int v[], int n)
//      {
//          int low, high, mid;
//          low = 0;
//          high = n - 1;
//          while (low <= high) {
//            mid = (low+high)/2;
//            if (x < v[mid])
//              high = mid -1 1;
//            else if (x > v[mid])
//              low = mid + 1;
//            else     /* found match */
//              return mid;
//          }
//          return -1; /* no match */
//      }

int binsearch_old(int x, int v[], int n);
int binsearch_new(int x, int v[], int n);

int main() {
  int sorted_array[]={1, 3, 5, 9, 17, 28, 31, 43, 56, 57, 63, 71, 79, 80, 89};
  /** old way **/
  printf("Result old_found %d\n", binsearch_old(9, sorted_array, 
        (int)sizeof(sorted_array)/sizeof(*sorted_array)));
  printf("Result old_not_found %d\n", binsearch_old(27, sorted_array, 
        (int)sizeof(sorted_array)/sizeof(*sorted_array)));
  /** new way **/
  printf("Result new_found %d\n", binsearch_new(9, sorted_array, 
        (int)sizeof(sorted_array)/sizeof(*sorted_array)));
  printf("Result new_not_found %d\n", binsearch_new(27, sorted_array, 
        (int)sizeof(sorted_array)/sizeof(*sorted_array)));
  return 0;
}

int binsearch_old(int x, int v[], int n)
{
  int low, high, mid;
  low = 0;
  high = n - 1;
  while (low <= high) {
    mid = (low+high)/2;
    if (x < v[mid])
      high = mid - 1;
    else if (x > v[mid])
      low = mid + 1;
    else     /* found match */
      return mid;
  }
  return -1; /* no match */
}

int binsearch_new(int x, int v[], int n)
{
  int low, high, mid;
  low = 0;
  high = n - 1;
  while (low < high) {
    mid = (low+high)/2;
    if (x > v[mid])
      low = mid + 1;
    else 
      high = mid;
  }
  return x==v[low]?low:-1; /* no match */
}
