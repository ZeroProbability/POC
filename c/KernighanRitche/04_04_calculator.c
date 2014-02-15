//  Exercise 4-3. Given the basic framework, it's straightforward to extend 
//  the calculator. Add the modulus (%) operator and provisions for negative 
//  numbers.
//
//  #include <stdio.h>
//  #include <stdlib.h> /* for atof() */
//                             
//  #define MAXOP 100 /* max size of operand or operator */
//  #define NUMBER  0 /* signal that a number was found */

//      int getop(char []);
//      void push(double);
//      double pop(void);

//      /* reverse Polish calculator */
//      main()
//      {
//        int type;
//        double op2;
//        char s[MAXOP];
//        while ((type = getop(s)) != EOF) {
//          switch (type) {
//            case NUMBER:
//              push(atof(s));
//              break;
//            case '+':
//              push(pop() + pop());
//              break;
//            case '*':
//              push(pop() * pop());
//              break;
//            case '-':
//              op2 = pop();
//              push(pop() - op2);
//              break;
//            case '/':
//              op2 = pop();
//              if (op2 != 0.0)
//                push(pop() / op2);
//              else
//                printf("error: zero divisor\n");
//              break;
//            case '\n':
//              printf("\t%.8g\n", pop());
//              break;
//            default:
//              printf("error: unknown command %s\n", s);
//              break;
//          }
//        }
//        return 0;
//      }

#include <stdio.h>
#include <stdlib.h> /* for atof() */
                         
#define MAXOP 100 /* max size of operand or operator */
#define NUMBER  0 /* signal that a number was found */

int getop(char []);
void push(double);
double pop(void);
double peek(void);
double peek_next(void);
void dup(void);
void swap(void);
void clear(void);

/* reverse Polish calculator */
int main()
{
    int type;
    double op2;
    char s[MAXOP];
    while ((type = getop(s)) != EOF) {
      switch (type) {
        case NUMBER:
          push(atof(s));
          break;
        case '+':
          push(pop() + pop());
          break;
        case '*':
          push(pop() * pop());
          break;
        case '-':
          op2 = pop();
          push(pop() - op2);
          break;
        case '/':
          op2 = pop();
          if (op2 != 0.0)
             push(pop() / op2);
          else
             printf("error: zero divisor\n");
          break;
        case '%':
          op2 = pop();
          if (op2 != 0.0)
            push((int)pop() % (int)op2);
          else
            printf("error: zero divisor\n");
          break;
        case '#':
          clear();
          printf("elements cleared\n");
          break;
        case '~':
          swap();
          printf("elements swaped\n");
          break;
        case ':':
          op2=peek();
          printf("top element = %lf\n", op2);
          break;
        case '"':
          op2=peek();
          push(op2);
          printf("top element = %lf\n", op2);
          printf("element duplicated= %lf\n", op2);
          break;
        case ';':
          op2=peek();
          printf("top element = %lf\n", op2);
          op2=peek_next();
          printf("next element = %lf\n", op2);
          break;
      case '\n':
        printf("\t%.8g\n", peek());
        break;
      default:
        printf("error: unknown command %s\n", s);
        break;
    }
  }
  return 0;
}

