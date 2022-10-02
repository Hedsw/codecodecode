#include <stdio.h>

int main()
{
	double avogadro = 6.022e23;

	puts("Large value with %f:");
	printf("%f\n",avogadro);
	puts("With the %e and %E placeholders:");
	printf("%e\n",avogadro);
	printf("%E\n",avogadro);
	puts("With %g and %G:");
	printf("%g\n",avogadro);
	printf("%G\n",avogadro);

	return(0);
}
