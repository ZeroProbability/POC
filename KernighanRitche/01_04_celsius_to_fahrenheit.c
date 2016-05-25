#include <stdio.h>

// Exercise 1-4. Write a program to print the corresponding Celsius to 
// Fahrenheit table.

int main() 
{
	float fahr, celsius;
	float lower, upper, step;

	lower = 0; /* lower limit of temperature scale */
	upper = 100; /* upper limit */
	step = 3; /* step size */
	celsius = lower;

	printf("%6s %6s\n", "Fahr", "Celsius");
	while (celsius <= upper) {
		fahr = (9.0/5.0) * celsius+32.0;
		printf("%6.2f %6.0f\n", fahr, celsius);
		celsius = celsius+step;
	}
	return 0;
}
