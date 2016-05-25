#include <stdio.h>
#define MAXVAL 100
int sp = 0;
double val[MAXVAL];

/* maximum depth of val stack */
/* next free stack position */
/* value stack */
/* push: push f onto value stack */
void push(double f)
{
  if (sp < MAXVAL)
      val[sp++] = f;
  else
    printf("error: stack full, can't push %g\n", f);
}

/* pop: pop and return top value from stack */
double pop(void)
{
  if (sp > 0)
    return val[--sp];
  else {
    printf("error: stack empty\n");
    return 0.0;
  }
}

double peek(void)
{
  if (sp > 0)
    return val[sp-1];
  else {
    printf("error: stack empty\n");
    return 0.0;
  }
}

double peek_next(void)
{
  if (sp > 1)
    return val[sp-2];
  else {
    printf("error: only one element in stack\n");
    return 0.0;
  }
}

void dup() 
{
    push(peek());
}

void clear(void)
{
  sp=0;
}

void swap(void)
{
  if(sp > 1){
    double v1=pop();
    double v2=pop();
    push(v1);
    push(v2);
  } else {
    printf("error: not enough elements to swap\n");
  }
}
