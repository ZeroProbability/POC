#include <stdio.h>

/* print Fahrenheit-Celsius table
for fahr = 0, 20, ..., 300; floating-point version */
float to_celsius(float);

int main()
{
	float fahr; 
	float lower, upper, step;

	lower = 0; /* lower limit of temperatuire scale */
	upper = 300; /* upper limit */
	step = 20; /* step size */

	fahr = lower;
	printf("%4s %6s\n", "fahr", "celsius");
	while (fahr <= upper) {
		printf("%4.0f %6.1f\n", fahr, to_celsius(fahr));
		fahr = fahr+step;
	}
	return 0;
}

float to_celsius(float fahr) {
    float celsius=(5.0/9.0) * (fahr-32.0);
    return celsius;
}
