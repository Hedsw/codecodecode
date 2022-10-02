#include <stdio.h>

int main()
{
	float a = 1234.5678;

	puts("Placeholder %f, no width specification:");
	printf("%f\n",a);
	puts("Width of 15 characters, %15f:");
	printf("%15f\n",a);
	puts("Width of 6 characters, 1 decimal place, %6.1f");
	printf("%6.1f\n",a);
	puts("No width, limit to 2 decimal places, %.2f");
	printf("%.2f\n",a);

	return(0);
}
